# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        mod = int(1e9) + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        last = {}

        for i in range(1, n + 1):
            dp[i] = (dp[i - 1] * 2) % mod
            if s[i - 1] in last:
                dp[i] -= dp[last[s[i - 1]] - 1]
            last[s[i - 1]] = i

        return (dp[n] - 1) % mod