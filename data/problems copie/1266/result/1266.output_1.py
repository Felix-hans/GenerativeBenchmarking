# @lc app=leetcode id=1266 lang=python3
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(len(points) - 1):
            curr_point = points[i]
            next_point = points[i + 1]
            x_diff = abs(curr_point[0] - next_point[0])
            y_diff = abs(curr_point[1] - next_point[1])
            total_time += max(x_diff, y_diff)  # Diagonal movement takes max(x_diff, y_diff) seconds
        return total_time