# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  # Sort the satisfaction array in non-decreasing order
        n = len(satisfaction)
        max_coefficient = 0
        total_time = 0

        for i in range(n - 1, -1, -1):
            if satisfaction[i] + total_time <= 0:
                break
            total_time += satisfaction[i]
            max_coefficient += total_time

        return max_coefficient