#!/usr/bin/python3

import unittest
from typing import Any, DefaultDict, Dict, List
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

You can do this by using an edge_to array. When doing a DFS, have the source_edge
be an index in the array and have the edge_to be the value in that index of
the array

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

    # TODO
    def detect_cycles(self, s: Any) -> bool:
        """Use DFS"""
        recursive_arr: Dict[str, List[Any]] = {}
        visited: List[bool] = []
        for v in self.graph:
            if self.detect_cycles_util(v, visited, recursive_arr):
                return True


        return True

    def detect_cycles_util(self, node: int, visited: List[bool], recursive_arr: List[Any]) -> bool:
        """DFS, if you go d
        """
        visited[node] = True
        recursive_arr[node] = True
        # TODO
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


    def DFSUtil(self, discovered: List[bool], v: int, edge_to: List[Any]) -> None:
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

        print ("Following is Breadth First Traversal"
                          " (starting from vertex 2)")
        g.BFS(2)
        g.DFS(2)

class ConnectedComponent:
    def __init__(self, graph: Graph) -> None:
        self.visited = List[str]
        self.graph = graph

    def construct_cc(self, graph: Graph) -> None:
        # v is the vertice
        for v, _ in self.graph.graph.items():
            if v not in self.visited:   # noqa
                self.visited[v] = True  # noqa
                self.DFS(any)

    def DFS(self, v: Any) -> None:

        pass



if __name__ == '__main__':
    unittest.main()
