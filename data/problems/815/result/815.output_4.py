# @lc app=leetcode id=815 lang=python3
from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        stop_to_routes = defaultdict(set)
        
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)
        
        visited_routes = set()
        
        queue = deque([(source, 0)])  # (bus stop, number of buses taken)
        
        while queue:
            curr_stop, num_buses = queue.popleft()
            
            if curr_stop == target:
                return num_buses
            
            for route_index in stop_to_routes[curr_stop]:
                if route_index not in visited_routes:
                    visited_routes.add(route_index)
                    
                    for stop in routes[route_index]:
                        queue.append((stop, num_buses + 1))
        
        return -1