# @lc app=leetcode id=329 lang=python3
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]
        max_length = 0
        
        for i in range(m):
            for j in range(n):
                length = self.dfs(matrix, i, j, memo)
                max_length = max(max_length, length)
        
        return max_length
    
    def dfs(self, matrix: List[List[int]], i: int, j: int, memo: List[List[int]]) -> int:
        if memo[i][j] != 0:
            return memo[i][j]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_length = 1
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                length = 1 + self.dfs(matrix, x, y, memo)
                max_length = max(max_length, length)
        
        memo[i][j] = max_length
        return max_length