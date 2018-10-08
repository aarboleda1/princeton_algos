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

"""


class Graph:
    def __init__(self) -> None:
        self.graph: DefaultDict[str, List[Any]] = defaultdict(list)
        self.edge_distance = 6

    def add_edge(self, u: Any, v: Any) -> None:
        """For a non directive graph, you can add the code:

        self.graph[v].append(u)
        because node A -> B means B -> A
        """
        self.graph[u].append(v)

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
        self.DFSUtil(discovered, v)

    def DFSUtil(self, discovered: List[bool], v: int) -> None:
        discovered[v] = True

        for neighbor in self.graph[str(v)]:
            if discovered[neighbor] is not False:
                print(f"visiting {neighbor}")
                self.DFS(neighbor)



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

if __name__ == '__main__':
    unittest.main()
