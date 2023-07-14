# @lc app=leetcode id=740 lang=python3
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        points = Counter(nums)
        max_num = max(nums)
        dp = [0] * (max_num + 1)

        for i in range(1, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * points[i])

        return dp[max_num]