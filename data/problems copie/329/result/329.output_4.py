# @lc app=leetcode id=329 lang=python3
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        memo = [[0] * n for _ in range(m)]  # Memoization table to store lengths
        
        def dfs(i: int, j: int) -> int:
            if memo[i][j] != 0:  # If the length is already calculated, return it
                return memo[i][j]
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible directions: right, left, down, up
            max_length = 1  # Minimum length is always 1
            
            for dx, dy in directions:
                x, y = i + dx, j + dy
                
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    length = 1 + dfs(x, y)  # Calculate length recursively
                    max_length = max(max_length, length)  # Update maximum length
            
            memo[i][j] = max_length  # Store the calculated length in the memoization table
            return max_length
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        
        return result