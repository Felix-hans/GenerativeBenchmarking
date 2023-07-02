# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7  # Modulo value

        dp = [0] * (len(s) + 1)

        dp[0] = 1

        last_occurrence = {}

        for i, c in enumerate(s, start=1):
            dp[i] = (2 * dp[i - 1]) % MOD  # Double the previous count

            if c in last_occurrence:
                dp[i] -= dp[last_occurrence[c] - 1]

            last_occurrence[c] = i

            dp[i] %= MOD

        return (dp[-1] - 1) % MOD