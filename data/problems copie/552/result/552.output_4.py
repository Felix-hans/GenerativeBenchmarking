# @lc app=leetcode id=552 lang=python3
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dpA = [0] * (n + 1)
        dpP = [0] * (n + 1)
        dpL = [0] * (n + 1)
        dpPL = [0] * (n + 1)

        dpP[0] = 1

        for i in range(1, n + 1):
            dpA[i] = (dpP[i - 1] + dpL[i - 1] + dpPL[i - 1]) % mod
            dpP[i] = (dpA[i - 1] + dpP[i - 1] + dpL[i - 1] + dpPL[i - 1]) % mod
            dpL[i] = dpP[i - 1] % mod
            dpPL[i] = dpL[i - 1] % mod