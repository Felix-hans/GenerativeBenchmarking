# @lc app=leetcode id=1184 lang=python3
from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total_distance = sum(distance)
        
        if start <= destination:
            clockwise_distance = sum(distance[start:destination])
        else:
            clockwise_distance = sum(distance[destination:start])
        
        counterclockwise_distance = total_distance - clockwise_distance
        
        return min(clockwise_distance, counterclockwise_distance)