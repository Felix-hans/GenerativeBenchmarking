# @lc app=leetcode id=2370 lang=python3
class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                diff = abs(ord(s[i]) - ord(s[j]))
                if diff <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)