#!/usr/bin/env python3

from typing import Any, DefaultDict, List
from collections import defaultdict


class DirectedEdge:
    def __init__(self, v: int, w: int, weight: float) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def from_(self) -> int:
        return self.v

    def to(self) -> int:
        return self.w

    def get_weight(self) -> float:
        return self.weight


class EdgeWeightedDigraph:
    def __init__(self, vertices: int) -> None:
        self.graph: DefaultDict[str, List[DirectedEdge]] = defaultdict(list)
        self.vertices = vertices
        self.build_graph()

        # for shortest_path API
        self.distances: List[int] = []
        self.edge_to: List[int] = []

    def build_graph(self) -> None:
        for i in range(self.vertices):
            self.graph[str(i)] = []

    def add_edge(self, edge: DirectedEdge) -> None:
        self.graph[str(edge.from_())].append(edge)

    def adj(self) -> List[int]:
        return []

    def dist_to(self, v: int) -> int:
        return self.distances[v]

    def path_to(self, v: int) -> List[int]:
        path: List[DirectedEdge] = []
        val = self.graph[str(v)]
        # TODO fixme
        edge = 1 # noqa
        while val is not None:
            path.append(edge) # noqa

        return path
