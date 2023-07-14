# @lc app=leetcode id=539 lang=python3
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            hour, minute = map(int, time.split(':'))
            minutes.append(hour * 60 + minute)

        minutes.sort()

        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            diff = minutes[i + 1] - minutes[i]
            min_diff = min(min_diff, diff)

        circular_diff = minutes[0] + (24 * 60) - minutes[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff