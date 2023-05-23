# @lc app=leetcode id=815 lang=python3
from typing import List, Dict, Set
from collections import deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        bus_stops = {}
        for i, route in enumerate(routes):
            for bus_stop in route:
                if bus_stop not in bus_stops:
                    bus_stops[bus_stop] = set()
                bus_stops[bus_stop].add(i)

        visited_stops = set()
        queue = deque([(source, 0)])

        while queue:
            bus_stop, num_buses = queue.popleft()

            if bus_stop == target:
                return num_buses

            for bus in bus_stops[bus_stop]:
                for next_stop in routes[bus]:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, num_buses + 1))

                del routes[bus]

        return -1