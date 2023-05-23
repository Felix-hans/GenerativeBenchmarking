# @lc app=leetcode id=329 lang=python3
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        longest_path = 0
        dp = [[0] * cols for _ in range(rows)]

        def dfs(row, col):
            if dp[row][col] != 0:
                return dp[row][col]

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_path = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] > matrix[row][col]:
                    max_path = max(max_path, dfs(new_row, new_col) + 1)

            dp[row][col] = max_path
            return max_path

        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path