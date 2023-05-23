# @lc app=leetcode id=740 lang=python3
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        num_freq = Counter(nums)
        max_num = max(nums)
        
        dp = [0] * (max_num + 1)
        
        dp[1] = num_freq[1]
        dp[2] = max(2 * num_freq[2], dp[1])
        
        for i in range(3, max_num + 1):
            dp[i] = max(i * num_freq[i] + dp[i - 2], dp[i - 1])
        
        return dp[max_num]