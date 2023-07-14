# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()  # Sort the dishes in ascending order

        max_coefficient = 0
        total_time = 0
        for i in range(n - 1, -1, -1):
            total_time += satisfaction[i]  # Add the current dish to the total time
            if total_time < 0:
                break  # If adding the current dish makes the total time negative, stop adding more dishes
            max_coefficient += total_time  # Add the like-time coefficient of the current dish to the maximum coefficient

        return max_coefficient