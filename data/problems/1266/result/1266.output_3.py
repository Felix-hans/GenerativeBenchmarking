# @lc app=leetcode id=1266 lang=python3
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            diagonal_distance = min(dx, dy)
            straight_distance = abs(dx - dy)
            total_time += diagonal_distance + straight_distance
        return total_time