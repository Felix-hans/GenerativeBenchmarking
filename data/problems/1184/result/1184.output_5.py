# @lc app=leetcode id=1184 lang=python3
from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = sum(distance)
        
        if start == destination:
            return 0
        
        if start > destination:
            start, destination = destination, start
        
        clockwise_distance = 0
        for i in range(start, destination):
            clockwise_distance += distance[i]
        
        counterclockwise_distance = total_distance - clockwise_distance
        
        return min(clockwise_distance, counterclockwise_distance)