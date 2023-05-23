# @lc app=leetcode id=539 lang=python3
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        time_points_in_minutes = [convert_to_minutes(time) for time in timePoints]
        time_points_in_minutes.sort()

        min_diff = float('inf')
        for i in range(len(time_points_in_minutes) - 1):
            diff = time_points_in_minutes[i + 1] - time_points_in_minutes[i]
            min_diff = min(min_diff, diff)

        circular_diff = (24 * 60 - time_points_in_minutes[-1]) + time_points_in_minutes[0]
        min_diff = min(min_diff, circular_diff)

        return min_diff