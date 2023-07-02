# @lc app=leetcode id=1425 lang=python3
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        max_sum = float('-inf')
        
        for i in range(n):
            max_sum = max(max_sum, dp[i-k] if i > k else 0)
            dp[i] = max(nums[i], nums[i] + max_sum)
        
        return max(dp)