# @lc app=leetcode id=1140 lang=python3
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}

        def dfs(start: int, M: int) -> int:
            if start >= len(piles):
                return 0
            
            if start + 2 * M >= len(piles):
                return sum(piles[start:])
            
            if (start, M) in memo:
                return memo[(start, M)]
            
            max_stones = 0
            for X in range(1, 2 * M + 1):
                Alice_stones = sum(piles[start:start+X])
                Bob_stones = dfs(start + X, max(M, X))
                max_stones = max(max_stones, Alice_stones + Bob_stones)
            
            memo[(start, M)] = max_stones
            return max_stones

        return dfs(0, 1)