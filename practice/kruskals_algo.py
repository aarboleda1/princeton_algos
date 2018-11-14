#!/usr/bin/env python3
from typing import Any, List, Union
"""
Kruskals Algorithm helps to build a minimum spanning tree which connects
all nodes in the minimum weight in a graph
https://www.hackerearth.com/blog/algorithms/kruskals-minimum-spanning-tree-algorithm-example/

Steps:
1. sort the graph edges w/ respect to their weights
2. Iterate thru the sorted edges and add the result IF and ONLY IF they do not
result in a cycle
If both edges do not belong to the same disjoint set, then add it to result
"""


class KruskalMST:
    def __init__(self) -> None:
        self.queue: List[Any] = []
        self.edge_weighted_graph: EdgeWeightedGraph = EdgeWeightedGraph()

    def construct_kruskal_mst(self) -> None:
        priority_queue: PriorityQueue = PriorityQueue()
        uf: UnionFind = UnionFind()
        # minimum spanning tree
        mst: List[Any] = []

        # create a sorted list of edge_weights
        for edge_weight in self.edge_weighted_graph.edges:
            priority_queue.append(edge_weight)

        while is_not_empty(priority_queue) and len(
                mst) < self.edge_weighted_graph.num_vertices() - 1:
            edge = priority_queue.delete_min()

            # get the two edges
            v = edge.either()  # noqa
            w = edge.other(v)  # noqa

            # If they are not connected, join them and add edge to mst
            if uf.connected(v, w) is False:
                uf.union(v, w)
                mst.append(edge)


def is_not_empty(list: Any) -> bool:
    return True


class EdgeWeightedGraph:
    def __init__(self) -> None:
        self.edges: List[Union[str, int]] = []

    def num_vertices(self) -> int:
        return 0

    def adjacent(self, v: int) -> List[int]:
        """Get neighbors for a vertex"""
        return []


class PriorityQueue:
    def __init__(self) -> None:
        self.pq: List[Union[str, int]] = []

    def append(self, val: Union[str, int]) -> None:
        self.pq.append(val)

    def delete_min(self) -> int:
        return 0


class UnionFind:
    def __init__(self) -> None:
        pass

    def connected(self, u: Any, v: Any) -> bool:
        return True

    def union(self, u: Any, v: Any) -> None:
        pass
