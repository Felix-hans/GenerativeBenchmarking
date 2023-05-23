# @lc app=leetcode id=815 lang=python3
from typing import List, Dict, Set
from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = self.buildGraph(routes)

        queue = deque([(source, 0)])
        visited = set([source])

        while queue:
            curr_stop, bus_count = queue.popleft()

            if curr_stop == target:
                return bus_count

            for neighbor in graph[curr_stop]:
                for bus in graph[curr_stop][neighbor]:
                    if bus not in visited:
                        visited.add(bus)
                        queue.append((neighbor, bus_count + 1))

        return -1

    def buildGraph(self, routes: List[List[int]]) -> Dict[int, Dict[int, Set[int]]]:
        graph = {}

        for bus, route in enumerate(routes):
            for stop in route:
                if stop not in graph:
                    graph[stop] = {}

                for neighbor in route:
                    if neighbor != stop:
                        if neighbor not in graph[stop]:
                            graph[stop][neighbor] = set()

                        graph[stop][neighbor].add(bus)

        return graph