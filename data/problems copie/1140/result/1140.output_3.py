# @lc app=leetcode id=1140 lang=python3
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}  # memoization table
        
        def stoneGameHelper(idx: int, M: int) -> int:
            if idx >= n:
                return 0
            
            if (idx, M) in memo:
                return memo[(idx, M)]
            
            max_stones = float('-inf')
            stones = 0
            for x in range(1, min(2*M + 1, n - idx + 1)):
                stones += piles[idx + x - 1]
                opponent_stones = stoneGameHelper(idx + x, max(M, x))
                max_stones = max(max_stones, stones - opponent_stones)
            
            memo[(idx, M)] = max_stones
            return max_stones
        
        return stoneGameHelper(0, 1)