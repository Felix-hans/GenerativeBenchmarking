# @lc app=leetcode id=1402 lang=python3
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort in descending order
        
        max_sum = 0
        total_time = 0
        
        for s in satisfaction:
            if total_time + s <= 0:
                break
            total_time += s
            max_sum += total_time
        
        return max_sum