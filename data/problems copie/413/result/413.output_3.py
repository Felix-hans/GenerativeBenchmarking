# @lc app=leetcode id=413 lang=python3
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        dp = [0] * len(nums)

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                count += dp[i]

        return count