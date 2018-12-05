#!/usr/bin/env python3

import json
from typing import TYPE_CHECKING, Any, Dict, List, MutableMapping, Optional, Tuple, cast

from bizapps.oracle_fusion.sync.common import FusionJSONDecoder, gather_with_exceptions
from bizapps.oracle_fusion.sync.fbid import generate_fbids
from bizapps.oracle_fusion.sync.mysql_connection import connect_shard
from bizapps.oracle_fusion.sync.sync_service.column_derivers.custom_column_deriver_base import (
    CustomColumnDeriverBase,
)
from bizapps.oracle_fusion.sync.sync_service.exceptions import (
    ColumnLookupException,
    ColumnValidationException,
)
from bizapps.oracle_fusion.sync.sync_service.types import Record
from libfb.py.asyncio.gen import genm
from libfb.py.asyncio.mysql import SQLRow

from .sync_strategy_with_insert import ProcessRecordException, SyncStrategyWithInsert
from .validator_base import ValidatorBase


if TYPE_CHECKING:
    from bizapps.oracle_fusion.sync.sync_info_types import SyncInfo  # noqa


class CustomColumnMappingWithFBID(SyncStrategyWithInsert):
    """Strategy class where column names from Fusion can be mapped to Intern
    """

    def __init__(
        self,
        dest_tier: str,
        dest_table: str,
        delay_seconds: float,
        col_key_dest: str,
        col_key_source: str,
        fbid_col: str,
        fbtype: int,
        column_map_direct: Optional[Dict[str, str]] = None,
        column_map_column_derivers: Optional[List[CustomColumnDeriverBase]] = None,
        column_validators: List[ValidatorBase] = None,
    ) -> None:
        """Args:
            col_key_source: Column name inside record from Oracle

            col_key_dest: Column name in destination table to see if record
            exists

            fbid_col: FBID column name

            column_map_direct: A dict of fusion column names where source (fusion)
                column names are the key, and value is the column name in dest
                (intern)

                E.g {"column_name_in_fusion": "column_name_in_intern"}

            dest_tier: Tier where data will be synced to
                E.g  "xdb.some_tier"

            dest_table: Table where data will be synced to
                E.g  "some_table"

            delay_seconds: Number of seconds between each query
        """
        self.col_key_source = col_key_source
        self.col_key_dest = col_key_dest
        self.fbid_col = fbid_col
        self.column_map_column_derivers = column_map_column_derivers or []
        self.column_map_direct = column_map_direct or {}
        super().__init__(dest_tier, dest_table, delay_seconds, column_validators)
    async def execute_sync_strategy(
        self, sync_info: "SyncInfo", mysql_tier: str
    ) -> None:
        records = await self.query_records_from_staging(mysql_tier, sync_info)
        await self.query_fbids(records)
        # (rows, exceptions) = await self.map_records(records)
        # await self.insert_into_dest_table(rows, sync_info)
        # await self.process_exceptions(exceptions, mysql_tier)

    async def query_fbids(self, records: List[Record]) -> Any:
        def get_key(staging_record: Record) -> Any:
            record = cast(Dict[str, Any], json.loads(staging_record.record, cls=FusionJSONDecoder))
            return record[self.col_key_source]
        if len([get_key(staging_record) for staging_record in records]) < 1:
            raise Exception(":OIH:OFEIHO:EIHF:OEIHF:OEIFH:OEIHF:OEIHF:EOIHFE:OIHF")
        values = ", ".join([get_key(staging_record) for staging_record in records])


        print(values)
        async with connect_shard(self.dest_tier) as mysql_conn:
            rows = await mysql_conn.query(
                f"""
                SELECT {self.col_key_dest}, {self.fbid_col} FROM {self.dest_table} WHERE IN ({values})
                """
            )
            print(rows)


    async def map_records(
        self, records: List[Record]
    ) -> Tuple[List[SQLRow], List[ProcessRecordException]]:
        await self.query_fbids(records)
        awaitables = [self.validate_and_map_record(record) for record in records]
        return await gather_with_exceptions(awaitables, ProcessRecordException)

    async def validate_and_map_record(
        self, staging_record: Record, **kwargs: Any
    ) -> SQLRow:
        record = cast(SQLRow, json.loads(staging_record.record, cls=FusionJSONDecoder))
        try:
            record = await self.map_record(record)

            if self.column_validators:
                for validator in self.column_validators:
                    validator.validate(record)
            return record
        except (ColumnLookupException, ColumnValidationException) as exception:
            """Raise ProcessRecordException, so that gather_with_exceptions will
            capture excpected exceptions here and then update the staging table
            """
            raise ProcessRecordException(exception, staging_record) from exception

    async def map_record(self, staging_record: SQLRow, **kwargs: Any) -> SQLRow:
        """Maps record with keys in destination table
        """
        # only make it mutable in this function
        record = cast(MutableMapping, staging_record)
        async with connect_shard(self.dest_tier) as mysql_conn:
            column_names = await mysql_conn.list_table_columns(self.dest_table)

        # execute custom lookups
        mapped_columns_from_function = await genm(
            {
                config.dest_column_name: config.gen_derive_column(
                    record[config.source_column_name]
                )
                for config in self.column_map_column_derivers
            }
        )

        def map_col_names(column_name: str) -> str:
            """Map column names in record to column names in dest_table
            """
            if column_name in self.column_map_direct:
                return self.column_map_direct[column_name]
            return column_name

        record = {
            map_col_names(column_name): record[column_name]
            for column_name in record.keys()
            if column_name in column_names
            or column_name in self.column_map_direct.keys()
        }
        record.update(mapped_columns_from_function)
        return record
