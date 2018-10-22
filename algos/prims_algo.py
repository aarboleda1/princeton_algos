#!/usr/bin/env python3
from typing import Any, List
from .kruskals_algo import EdgeWeightedGraph
"""Prims Algorithm

Another implementation to find a minimum spanning tree in a graph

- Start with a vertex and greedily grow a tree
- Use a priority queue of all the edges and then their weights
- Iterate thru each edge, and then add to T the edge w the minimum weight that
connects to T that does not cause a cycle and as long as it's less than v - 1
edges
"""


class Edge:
    def __init__(self, v: int, w: int) -> None:
        self.v = v
        self.w = w

    def other(self, v: int) -> int:
        return v if v == self.v else self.w


class LazyPrimMST:
    def __init__(self) -> None:
        # queue
        self.mst: List[Edge] = []
        # MST vertices
        self.visited: List[bool] = []
        # This should actually be a priority queue
        self.pq: List[Edge] = []

    # assume graph is connected
    def lazy_prim_mst(self, graph: EdgeWeightedGraph) -> None:
        self.visit(graph, 0)
        while len(self.pq) > 0:
            edge = self.pq.pop(0)
            v = edge.v
            w = edge.w

            # If they are both marked, they are already on the MST
            if self.visited[v] is True or self.visited[w] is True:
                self.mst.append(edge)
                if self.visited[v] is False:
                    self.visit(graph, v)

                if self.visited[w] is False:
                    self.visit(graph, w)

    def visit(self, graph: EdgeWeightedGraph, v: int) -> None:
        self.visited[v] = True
        if v not in self.visited:
            self.visited[v] = True
            # Importatnt!!!
            # Add an edge to the priority queue by checking if the other edges
            # has not been visited yet
            for edge in graph.adjacent(v):
                if self.visited[edge.other(v)] is False:
                    self.pq.append(edge)
