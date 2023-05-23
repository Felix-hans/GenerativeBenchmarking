# @lc app=leetcode id=1594 lang=python3
class Solution:
    def maxProductPath(self, grid):
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7

        max_product = [[0] * n for _ in range(m)]
        min_product = [[0] * n for _ in range(m)]

        max_product[0][0] = min_product[0][0] = grid[0][0]

        for j in range(1, n):
            max_product[0][j] = min_product[0][j] = max_product[0][j - 1] * grid[0][j]

        for i in range(1, m):
            max_product[i][0] = min_product[i][0] = max_product[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] < 0:
                    max_product[i][j] = min(max_product[i - 1][j], max_product[i][j - 1]) * grid[i][j]
                    min_product[i][j] = max(max_product[i - 1][j], max_product[i][j - 1]) * grid[i][j]
                else:
                    max_product[i][j] = max(max_product[i - 1][j], max_product[i][j - 1]) * grid[i][j]
                    min_product[i][j] = min(min_product[i - 1][j], min_product[i][j - 1]) * grid[i][j]

        result = max_product[-1][-1]
        if result < 0:
            return -1
        else:
            return result % mod