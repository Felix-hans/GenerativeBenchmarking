# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        last = [-1] * 26
        MOD = int(1e9) + 7

        dp[0] = 1
        for i in range(n):
            dp[i + 1] = (2 * dp[i] - (dp[last[ord(s[i])] - 1] if last[ord(s[i])] >= 0 else 0)) % MOD
            last[ord(s[i])] = i

        return (dp[n] - 1) % MOD