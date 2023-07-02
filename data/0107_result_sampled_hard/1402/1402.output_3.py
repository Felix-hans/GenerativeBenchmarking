# @lc app=leetcode id=1402 lang=python3
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  # Sort the satisfaction values in non-decreasing order
        n = len(satisfaction)
        max_sum = 0
        total_time = 0
        
        for i in range(n - 1, -1, -1):
            if satisfaction[i] + total_time > 0:
                total_time += satisfaction[i]
                max_sum += total_time
            
        return max_sum