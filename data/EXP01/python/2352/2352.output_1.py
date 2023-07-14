# @lc app=leetcode id=2352 lang=python3
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == list(map(lambda x: x[j], grid)):
                    count += 1
        return count