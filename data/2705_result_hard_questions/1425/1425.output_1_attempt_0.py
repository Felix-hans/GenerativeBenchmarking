# @lc app=leetcode id=1425 lang=python3
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n  # dp[i] represents the maximum sum of subsequence ending at index i
        dp[0] = nums[0]  # Base case: the maximum sum at the first index is the number itself
        
        max_sum = dp[0]  # Variable to keep track of the maximum sum
        
        for i in range(1, n):
            max_prev_sum = max(dp[max(0, i-k):i])
            
            dp[i] = max(nums[i], nums[i] + max_prev_sum)
            
            max_sum = max(max_sum, dp[i])
        
        return max_sum