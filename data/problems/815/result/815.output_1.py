# @lc app=leetcode id=815 lang=python3
from collections import deque, defaultdict
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        bus_stops = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
                bus_stops[stop].append(i)

        queue = deque([(source, 0)])
        visited_buses = set()
        visited_stops = set([source])

        while queue:
            stop, buses_taken = queue.popleft()

            if stop == target:
                return buses_taken

            for bus in bus_stops[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))

        return -1