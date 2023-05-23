# @lc app=leetcode id=1594 lang=python3
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_product = [[0] * n for _ in range(m)]
        min_product = [[0] * n for _ in range(m)]

        max_product[0][0] = min_product[0][0] = grid[0][0]

        for j in range(1, n):
            max_product[0][j] = min_product[0][j] = max_product[0][j - 1] * grid[0][j]

        for i in range(1, m):
            max_product[i][0] = min_product[i][0] = max_product[i - 1][0] * grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    max_product[i][j] = max(max_product[i - 1][j], max_product[i][j - 1]) * grid[i][j]
                    min_product[i][j] = min(min_product[i - 1][j], min_product[i][j - 1]) * grid[i][j]
                else:
                    max_product[i][j] = min(min_product[i - 1][j], min_product[i][j - 1]) * grid[i][j]
                    min_product[i][j] = max(max_product[i - 1][j], max_product[i][j - 1]) * grid[i][j]

        max_product_value = max_product[m - 1][n - 1] % (10 ** 9 + 7)
        if max_product_value < 0:
            return -1
        else:
            return max_product_value