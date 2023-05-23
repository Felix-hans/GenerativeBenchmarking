# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  # Sort the satisfaction array in ascending order
        max_coef = 0
        total_coef = 0

        for i, s in enumerate(satisfaction):
            curr_coef = (i + 1) * s
            total_coef += curr_coef

            if total_coef <= 0:
                return 0

            max_coef = max(max_coef, total_coef)

        return max_coef