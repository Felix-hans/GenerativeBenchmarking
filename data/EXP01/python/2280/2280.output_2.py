# @lc app=leetcode id=2280 lang=python3
from typing import List

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n == 0:
            return 0

        lines = 1
        for i in range(1, n):
            if stockPrices[i][1] != stockPrices[i-1][1]:
                lines += 1
        
        return lines