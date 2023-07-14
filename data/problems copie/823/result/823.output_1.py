# @lc app=leetcode id=823 lang=python3
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        arr.sort()  # Sort the array in ascending order
        n = len(arr)
        dp = [1] * n  # Initialize dp array with all elements set to 1

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    dp[i] = (dp[i] + dp[j] * dp.get(arr[i] // arr[j], 0)) % MOD

        return sum(dp) % MOD