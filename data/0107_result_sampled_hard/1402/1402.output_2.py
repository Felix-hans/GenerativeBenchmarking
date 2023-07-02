# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort satisfaction values in descending order
        total = 0  # Variable to track the total like-time coefficient
        max_coefficient = 0  # Variable to track the maximum like-time coefficient

        for s in satisfaction:
            if total + s > 0:
                total += s
                max_coefficient += total
            else:
                break

        return max_coefficient