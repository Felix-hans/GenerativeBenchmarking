# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last_occurrence = {}
        mod = int(1e9 + 7)

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod

            if s[i - 1] in last_occurrence:
                j = last_occurrence[s[i - 1]]
                dp[i] = (dp[i] - dp[j]) % mod

            last_occurrence[s[i - 1]] = i - 1

        return (dp[n] - 1) % mod