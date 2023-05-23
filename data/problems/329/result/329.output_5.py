# @lc app=leetcode id=329 lang=python3
from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]  # Memoization matrix to store lengths
        
        def dfs(i, j):
            if memo[i][j] != 0:
                return memo[i][j]
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions to move
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    memo[i][j] = max(memo[i][j], dfs(x, y))
            
            memo[i][j] += 1  # Add 1 to the length starting from the current cell
            return memo[i][j]
        
        longest_path = 0
        
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))
        
        return longest_path