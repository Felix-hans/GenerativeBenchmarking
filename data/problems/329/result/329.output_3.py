# @lc app=leetcode id=329 lang=python3
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        cache = [[0] * n for _ in range(m)]
        max_length = 0

        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    cache[i][j] = max(cache[i][j], dfs(x, y))

            cache[i][j] += 1
            return cache[i][j]

        for i in range(m):
            for j in range(n):
                max_length = max(max_length, dfs(i, j))

        return max_length