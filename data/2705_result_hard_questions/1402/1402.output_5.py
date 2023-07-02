# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort dishes in descending order of satisfaction
        
        max_coefficient = 0  # Maximum like-time coefficient
        total_time = 0  # Total time taken to cook the dishes
        
        for s in satisfaction:
            if total_time + s <= 0:
                break  # Stop cooking further dishes if adding the current dish decreases the coefficient
            total_time += s
            max_coefficient += total_time
        
        return max_coefficient