# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        mod = 10**9 + 7
        dp = [0] * (n + 1)
        last = [-1] * 26
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i-1]) % mod
            if last[ord(s[i-1]) - ord('a')] != -1:
                dp[i] -= dp[last[ord(s[i-1]) - ord('a')]]
            dp[i] %= mod
            last[ord(s[i-1]) - ord('a')] = i - 1

        return (dp[n] - 1) % mod