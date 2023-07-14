# @lc app=leetcode id=1425 lang=python3
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            max_prev_sum = max(dp[max(0, i - k):i])
            dp[i] = max(max_prev_sum, 0) + nums[i]  # Take the maximum sum and add nums[i]
            max_sum = max(max_sum, dp[i])  # Update the maximum sum if necessary

        return max_sum