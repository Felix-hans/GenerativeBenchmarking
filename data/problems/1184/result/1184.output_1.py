# @lc app=leetcode id=1184 lang=python3
from typing import List

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        total_distance = sum(distance)
        clockwise_distance = 0
        counterclockwise_distance = 0

        if start <= destination:
            clockwise_distance = sum(distance[start:destination])
        else:
            clockwise_distance = sum(distance[start:]) + sum(distance[:destination])

        if start >= destination:
            counterclockwise_distance = sum(distance[destination:start])
        else:
            counterclockwise_distance = sum(distance[destination:]) + sum(distance[:start])

        return min(clockwise_distance, counterclockwise_distance)