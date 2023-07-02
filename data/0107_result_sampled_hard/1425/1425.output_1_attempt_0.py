# @lc app=leetcode id=1425 lang=python3
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n  # dp[i] stores the maximum sum of subsequence ending at nums[i]

        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            max_prev_sum = max(dp[i-j] for j in range(1, min(k, i) + 1))
            dp[i] = max(max_prev_sum + nums[i], nums[i])  # Update dp[i] with the maximum sum
            max_sum = max(max_sum, dp[i])  # Update the maximum sum so far

        return max_sum