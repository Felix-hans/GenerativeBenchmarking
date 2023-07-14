# @lc app=leetcode id=815 lang=python3
from collections import deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        stop_to_routes = {}
        for bus_route in routes:
            for stop in bus_route:
                if stop not in stop_to_routes:
                    stop_to_routes[stop] = set()
                stop_to_routes[stop].add(tuple(bus_route))

        visited_stops = set()
        queue = deque([(source, 0)])  # (bus_stop, bus_changes)
        
        while queue:
            current_stop, bus_changes = queue.popleft()
            
            if current_stop == target:
                return bus_changes
            
            routes_passing_through_stop = stop_to_routes.get(current_stop, [])
            
            for route in routes_passing_through_stop:
                for next_stop in route:
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        queue.append((next_stop, bus_changes + 1))
                
                for stop, routes_set in stop_to_routes.items():
                    if route in routes_set:
                        routes_set.remove(route)
        
        return -1