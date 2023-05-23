# @lc app=leetcode id=1594 lang=python3
class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        max_prod = [[0] * n for _ in range(m)]
        min_prod = [[0] * n for _ in range(m)]
        
        max_prod[0][0] = min_prod[0][0] = grid[0][0]
        
        for i in range(1, m):
            max_prod[i][0] = min_prod[i][0] = max_prod[i-1][0] * grid[i][0]
        
        for j in range(1, n):
            max_prod[0][j] = min_prod[0][j] = max_prod[0][j-1] * grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] < 0:
                    max_prod[i][j] = min(min_prod[i-1][j], min_prod[i][j-1]) * grid[i][j]
                    min_prod[i][j] = max(max_prod[i-1][j], max_prod[i][j-1]) * grid[i][j]
                else:
                    max_prod[i][j] = max(max_prod[i-1][j], max_prod[i][j-1]) * grid[i][j]
                    min_prod[i][j] = min(min_prod[i-1][j], min_prod[i][j-1]) * grid[i][j]
        
        max_prod_mod = max_prod[-1][-1] % (10**9 + 7)
        
        if max_prod_mod < 0:
            return -1
        else:
            return max_prod_mod