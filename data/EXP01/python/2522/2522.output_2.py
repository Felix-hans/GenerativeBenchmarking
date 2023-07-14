# @lc app=leetcode id=2522 lang=python3
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        dp = [float('inf')] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(i, -1, -1):
                if int(s[j:i+1]) <= k:
                    dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[n-1] if dp[n-1] != float('inf') else -1