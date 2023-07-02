# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort in descending order
        
        max_sum = 0  # Maximum sum of like-time coefficients
        total_time = 0  # Total time taken
        
        for s in satisfaction:
            if total_time + s <= 0:
                break  # If adding the current dish decreases the total time, stop adding more dishes
            
            total_time += s
            max_sum += total_time
        
        return max_sum