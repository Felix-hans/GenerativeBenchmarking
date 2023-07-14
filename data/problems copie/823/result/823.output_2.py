# @lc app=leetcode id=823 lang=python3
class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()  # Sort the array in ascending order

        n = len(arr)
        dp = [1] * n  # Initialize the dp array with 1 (each number can form a tree by itself)

        index = {x: i for i, x in enumerate(arr)}  # Map each number to its index for quick lookup

        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    y = x // arr[j]  # Calculate the other factor
                    if y in index:
                        dp[i] += dp[j] * dp[index[y]]  # Add the product of the number of trees for both factors

            dp[i] %= MOD  # Take the modulo to avoid overflow

        return sum(dp) % MOD  # Return the sum of all counts modulo 10^9 + 7