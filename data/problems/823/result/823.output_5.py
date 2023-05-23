# @lc app=leetcode id=823 lang=python3
class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()  # Sort the array in ascending order
        dp = {}  # Dictionary to store the count of binary trees for each integer

        for i in range(len(arr)):
            dp[arr[i]] = 1  # Initialize the count to 1 for each individual integer
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    factor = arr[i] // arr[j]
                    if factor in dp:
                        dp[arr[i]] += dp[arr[j]] * dp[factor]
                        dp[arr[i]] %= MOD

        total_count = sum(dp.values()) % MOD  # Calculate the total count of binary trees
        return total_count