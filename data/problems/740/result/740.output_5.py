# @lc app=leetcode id=740 lang=python3
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * 10001  # Initialize frequency array
        
        for num in nums:
            freq[num] += num
        
        dp = [0] * 10001  # Initialize dp array
        
        dp[0] = 0
        dp[1] = freq[1]
        
        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2] + freq[i])
        
        return dp[10000]