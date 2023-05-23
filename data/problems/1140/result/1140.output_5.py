# @lc app=leetcode id=1140 lang=python3
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        prefix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            prefix_sum[i] = prefix_sum[i+1] + piles[i]

        memo = {}  # memoization dictionary

        def dp(start, M):
            if start + 2 * M >= n:  # can take all remaining stones
                return prefix_sum[start]
            if (start, M) in memo:
                return memo[(start, M)]

            max_stones = 0
            for x in range(1, 2 * M + 1):
                next_start = start + x
                max_stones = max(max_stones, prefix_sum[start] - dp(next_start, max(M, x)))

            memo[(start, M)] = max_stones
            return max_stones

        return dp(0, 1)