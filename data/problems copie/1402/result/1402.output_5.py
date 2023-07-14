# @lc app=leetcode id=1402 lang=python3
from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort dishes in descending order
        n = len(satisfaction)
        max_like_time = 0
        curr_time = 0
        
        for i in range(n):
            if curr_time + satisfaction[i] <= 0:
                break  # Stop if adding the next dish makes the like-time coefficient negative
            curr_time += satisfaction[i]
            max_like_time += curr_time
        
        return max_like_time