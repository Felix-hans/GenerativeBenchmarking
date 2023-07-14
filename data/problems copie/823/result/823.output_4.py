# @lc app=leetcode id=823 lang=python3
class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()  # Sort the array in ascending order
        n = len(arr)
        dp = [1] * n  # Initialize the dynamic programming array with 1's

        index = {num: i for i, num in enumerate(arr)}

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    complement = arr[i] // arr[j]
                    if complement in index:
                        dp[i] += dp[j] * dp[index[complement]]
                        dp[i] %= MOD

        total_count = sum(dp) % MOD
        return total_count