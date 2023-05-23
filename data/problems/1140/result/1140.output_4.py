# @lc app=leetcode id=1140 lang=python3
class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        memo = [[-1] * (2 * n) for _ in range(n)]  # Memoization table

        def dp(i, M):
            if i >= n:  # Base case: no more piles left
                return 0

            if memo[i][M] != -1:  # Check if the result is already computed
                return memo[i][M]

            max_stones = float('-inf')

            for x in range(1, 2 * M + 1):
                if i + x <= n:
                    stones = sum(piles[i:i + x])
                    max_stones = max(max_stones, stones - dp(i + x, max(x, M)))

            memo[i][M] = max_stones  # Store the result in the memoization table
            return max_stones

        return dp(0, 1)