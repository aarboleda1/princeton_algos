#!/usr/bin/python3

import unittest
from typing import Any, DefaultDict, List
from collections import defaultdict
"""Course Notes:

10/8

Graph processing problems:
- shortest_path
- connectivity
- planarity - can you draw the graph in the plane with no crossing edges?


10/10 Graph processing
Design Pattern
- Create a Graph Object
- Pass the graph to a processing routine
- Query the graph-processing routine for information

To get a path from node s to v, use a stack

You can do this by using an edge_to array. When doing a DFS, have the
source_edge be an index in the array and have the edge_to be the value
in that index of the array

for (let x = vertex; x != source_edge; x = edge_to[vertex]) {
    path.push(x)
}

10/11 Graph Processing
BFS Properties

Proposition: BFS computes shortest path (fewest number of edges) from s to
all other vertices in a graph in time proportional E + V

Proof: The Queue used for BFS always consists of zero or more vertices of
distance k from s, followed by zero or more vertices of distance k + 1

10/12

Connected Components

Proposition: You can use a DFS in a graph to find out how many connected
components there are in a graph

1: 2, 3, 4
2: 3
4: 2
6: 7, 8

There are 2 connected components in this see below

10/14

Longest Path in a DAG

Topological Sorting

"""


# Undirected
class Graph:
    def __init__(self) -> None:
        self.graph: DefaultDict[str, List[Any]] = defaultdict(list)
        self.edge_distance = 6

    def add_edge(self, u: Any, v: Any) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)

    def distance_to(self, u: Any, v: Any) -> int:
        """Time Complexity:

        This algorithm takes O(V+E) where E is the number of edges in the
        connected component of a. The worst case occurs when the graph is
        complete, which would result in O(N2).
        """
        #  http://www.studies.nawaz.org/posts/breadth-first-search-and-finding-the-distance-between-two-nodes/
        """Modified BFS"""
        distances: List[int] = [-1] * len(self.graph)
        queue: List[Any] = []
        distance = 0
        # mark as visited, has no incoming edges
        distances[u] = distance
        queue.append(u)

        while len(queue) > 0:
            node = queue.pop(0)
            distance = distance + 1
            for neighbor in self.graph[node]:
                if distances[neighbor] == -1:
                    queue.append(node)
                    distances[neighbor] = distance

        return 0

    def detect_cycles(self, s: Any) -> bool:
        """Use DFS"""
        recursive_arr: List[bool] = []
        visited: List[bool] = []
        for v in self.graph:
            if self.detect_cycles_util(v, visited, recursive_arr) is False:
                return False
        return True

    def detect_cycles_util(self, v: str, visited: List[bool],
                           recursive_arr: List[bool]) -> bool:
        """Use a recursion_arr to keep track of the current call stack
        """
        visited[int(v)] = True
        recursive_arr[int(v)] = True
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.detect_cycles_util(neighbor, visited, recursive_arr):
                    return True
            elif visited[neighbor] and recursive_arr[neighbor]:
                return True
        recursive_arr[int(v)] = False
        return False

    def detect_cycles_undirected(self, s: Any) -> bool:
        return False

    def detect_cycles_undirected_util(self) -> bool:
        return True

    def shortest_path(self, startId: int) -> List[int]:
        distances: List[int] = [-1] * len(self.graph)
        queue: List[int] = []
        queue.append(startId)
        # distances from startId to s is zero
        distances[startId] = 0
        while len(queue) > 0:
            node = queue.pop(0)
            for neighbor in self.graph[str(node)]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[node] + self.edge_distance
                    queue.append(neighbor)
        return distances
        pass

    def BFS(self, s: Any) -> None:
        discovered: List[bool] = [False] * (len(self.graph))
        queue: List[Any] = []

        queue.append(s)
        discovered[s] = True
        while len(queue) > 0:
            s = queue.pop(0)
            for i in self.graph[s]:
                if discovered[i] is not False:
                    queue.append(i)
                    discovered[i] = True

    def DFS(self, v: Any) -> None:
        discovered: List[bool] = [False] * (len(self.graph))
        edge_to: List[Any] = []
        self.DFSUtil(discovered, v, edge_to)

    def DFSUtil(self, discovered: List[bool], v: int,
                edge_to: List[Any]) -> None:
        discovered[v] = True

        for neighbor in self.graph[str(v)]:
            if discovered[neighbor] is not False:
                print(f"visiting {neighbor}")
                self.DFS(neighbor)
                edge_to[neighbor] = v


class GraphTest(unittest.TestCase):
    def test_bfs(self):
        g = Graph()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 3)

        print("Following is Breadth First Traversal"
              " (starting from vertex 2)")
        g.BFS(2)


class ConnectedComponent:
    """Returns a ConnectedComponent and strongly connected component of graph
    """

    def __init__(self, graph: Graph) -> None:
        self.visited: List[bool] = []
        self.graph = graph
        self.count = 0
        # indexs are the vertices, values at indesx are the
        # id of the connected component they are apart of
        self.cc_ids: List[int] = []

    def cc(self, graph: Graph) -> None:
        # v is the vertice
        for v, _ in self.graph.graph.items():
            if v not in self.visited:
                self.DFS(int(v))
                self.count += 1

    def strongly_cc(self, graph: Graph) -> None:
        """Kosaraju-Sharir Strongly Connected Component
        """
        # Get the reverse post orderof the graph
        reverse_post_order = self.get_reverse_post_order()
        for v in reverse_post_order:
            if v not in self.visited:
                self.DFS(int(v))
                self.count += 1

    def DFS(self, v: int) -> None:
        self.visited[v] = True
        self.cc_ids[v] = self.count
        for neighbor in self.graph.graph:
            if neighbor not in self.visited:
                self.DFS(int(neighbor))

    def get_reverse_post_order(self) -> List[int]:
        """Should return the reverse post order of the graph
        """
        ordering_arr: List[int] = []
        visited: List[bool] = []
        for v in self.graph.graph:
            if int(v) not in visited:
                self.get_reverse_post_order_util(int(v), visited, ordering_arr)
        return ordering_arr

    def get_reverse_post_order_util(
        self, v: int,
        visited: List[bool],
        ordering_arr: List[int]
    ) -> None:
        visited[v] = True
        for neighbor in self.graph.graph[str(v)]:
            if neighbor not in visited:
                self.get_reverse_post_order_util(
                    neighbor, visited, ordering_arr
                )
        ordering_arr.append(int(v))


if __name__ == '__main__':
    unittest.main()
