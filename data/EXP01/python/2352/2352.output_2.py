# @lc app=leetcode id=2352 lang=python3
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        for i in range(n):
            for j in range(n):
                if grid[i] == [row[j] for row in grid]:
                    count += 1
        return count