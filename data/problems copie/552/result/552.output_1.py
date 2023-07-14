# @lc app=leetcode id=552 lang=python3
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        dp_A = [0] * n
        dp_P = [0] * n

        dp_A[0] = 1
        dp_P[0] = 1

        if n > 1:
            dp_L = [0] * n
            dp_L[1] = 1

        for i in range(1, n):
            dp_P[i] = (dp_A[i - 1] + dp_P[i - 1] + (dp_L[i - 1] if i > 1 else 0)) % MOD
            dp_A[i] = (dp_P[i - 1] + (dp_P[i - 2] if i > 1 else 0)) % MOD
            if i > 1:
                dp_L[i] = (dp_A[i - 1] + dp_A[i - 2]) % MOD

        total = (dp_A[n - 1] + dp_P[n - 1] + (dp_L[n - 1] if n > 1 else 0)) % MOD

        return total