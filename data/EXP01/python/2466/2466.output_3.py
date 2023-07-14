# @lc app=leetcode id=2466 lang=python3
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        dp = [[[0 for _ in range(2)] for _ in range(one + 1)] for _ in range(zero + 1)]
        dp[0][0][0] = 1

        for i in range(zero + 1):
            for j in range(one + 1):
                for k in range(2):
                    if i > 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i-1][j][0]) % mod
                    if j > 0:
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j-1][1]) % mod
                    if k == 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i][j][1]) % mod
                    elif k == 1:
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j][0]) % mod

        ans = 0
        for i in range(low, high + 1):
            ans = (ans + dp[zero][one][0] + dp[zero][one][1]) % mod

        return ans