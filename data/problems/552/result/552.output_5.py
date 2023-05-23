# @lc app=leetcode id=552 lang=python3
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dp_A = [0] * (n + 1)
        dp_P = [0] * (n + 1)
        dp_L = [0] * (n + 1)

        dp_A[0] = 1
        dp_P[0] = 1
        dp_L[0] = 1
        dp_P[1] = 1
        dp_L[1] = 1
        dp_L[2] = 3

        for i in range(1, n + 1):
            dp_A[i] = (dp_P[i - 1] + dp_L[i - 1] + dp_A[i - 1]) % MOD
            if i > 1:
                dp_P[i] = (dp_A[i - 1] + dp_L[i - 1] + dp_P[i - 1]) % MOD
            if i > 2:
                dp_L[i] = (dp_A[i - 1] + dp_P[i - 1] + dp_A[i - 2] + dp_P[i - 2]) % MOD

        return (dp_A[n] + dp_P[n] + dp_L[n]) % MOD