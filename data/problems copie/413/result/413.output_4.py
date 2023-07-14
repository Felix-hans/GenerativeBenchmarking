# @lc app=leetcode id=413 lang=python3
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        dp = [0] * n  # dp[i] stores the number of arithmetic subarrays ending at index i
        count = 0  # total count of arithmetic subarrays
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                count += dp[i]
        
        return count