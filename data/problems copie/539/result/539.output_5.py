# @lc app=leetcode id=539 lang=python3
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(':'))
            return hours * 60 + minutes

        time_points = sorted(map(time_to_minutes, timePoints))
        min_diff = float('inf')

        for i in range(len(time_points)):
            diff = time_points[(i + 1) % len(time_points)] - time_points[i]
            min_diff = min(min_diff, diff)

        return min_diff