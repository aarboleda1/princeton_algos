#!/usr/bin/env python3
"""
This API provides all shortest paths starting from source

It's very similar to Prim's algorithm but this is meant for
directed graphs

- Consider all vertices in increasing order of distance from s
- For each vertex:
    - Add to the edgeTo and distTo array
    - Also, relax all edges pointing FROM each edge
"""
from typing import Any, List
from math import inf


class DjikstrasShortestPath:
    def __init__(self) -> None:
        self.edge_to: List[Any] = []  # should be List[DirectedEdge]
        self.dist_to: List[float] = []
        self.pq: List[Any] = []  # priority queue

    def shortest_path(self, G: Any, s: int) -> None:
        """Calculates shortest path
        G: EdgeWeightedGraph
        s: source vertice
        """
        # Mark each dist_to as inf, we'll be greedily finding a better way to
        # get to each vertice
        for v in range(G.num_vertices()):
            self.dist_to[v] = inf

        # dist from source to source it 0
        self.dist_to[s] = 0.0
        self.pq[s] = (0, 0)

        while len(self.pq) > 0:
            v = pq.del_min()
            for edge_from_v in G.adj(v):
                self.relax(edge_from_v)

    def relax(self, edge: Any) -> None:
        """edge: DirectedEdge"""
        v = edge.from_()
        w = edge.to()

        # Greedily update the dist_to array
        if self.dist_to[w] > self.dist_to[v] + edge.weight:
            self.dist_to[w] = self.dist_to[v] + edge.weight
            self.edge_to = edge

            # Relax edge by updating self.dist_to to be a shorter distance
            # or insert it if we haven't seen it yet
            self.pq.decreaseKey(w, self.dist_to[w]) if self.pq.contains(w # noqa
                w) else self.pq.append(edge) # noqa
