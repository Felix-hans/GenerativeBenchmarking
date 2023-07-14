# @lc app=leetcode id=552 lang=python3
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(n + 1)]

        dp[0][0] = 1  # A = 0, L = 0
        dp[1][0] = 1  # A = 1, L = 0
        dp[0][1] = 1  # A = 0, L = 1

        for i in range(2, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD

            dp[i][1] = (dp[i - 1][0] + dp[i - 2][0]) % MOD

            dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD

        total_records = sum(dp[n]) % MOD

        return total_records