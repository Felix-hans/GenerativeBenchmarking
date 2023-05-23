# @lc app=leetcode id=1594 lang=python3
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_pos = [[0] * n for _ in range(m)]
        max_neg = [[0] * n for _ in range(m)]

        max_pos[0][0] = max_neg[0][0] = grid[0][0]

        for j in range(1, n):
            max_pos[0][j] = max_pos[0][j-1] * grid[0][j]
            max_neg[0][j] = max_neg[0][j-1] * grid[0][j]

        for i in range(1, m):
            max_pos[i][0] = max_pos[i-1][0] * grid[i][0]
            max_neg[i][0] = max_neg[i-1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    max_pos[i