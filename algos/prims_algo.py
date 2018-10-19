#!/usr/bin/env python3
from typing import Any, List
"""Prims Algorithm

Another implementation to find a minimum spanning tree in a graph
"""
class Edge:
    pass

class LazyPrimMST:
    def __init__(self) -> None:
        self.marked: List[Any] = []
        self.mst: List[Edge] = []
