# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort in descending order
        n = len(satisfaction)
        max_coefficient = 0
        total_time = 0
        
        for i in range(n):
            if total_time + satisfaction[i] < 0:
                break  # Stop if adding the next dish decreases the coefficient
            total_time += satisfaction[i]
            max_coefficient += total_time
        
        return max_coefficient