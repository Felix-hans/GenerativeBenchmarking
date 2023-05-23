# @lc app=leetcode id=823 lang=python3
class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {}

        for i, num in enumerate(arr):
            dp[num] = 1
            for j in range(i):
                if num % arr[j] == 0:
                    other_factor = num // arr[j]
                    if other_factor in dp:
                        dp[num] += dp[arr[j]] * dp[other_factor]
                        dp[num] %= MOD

        return sum(dp.values()) % MOD