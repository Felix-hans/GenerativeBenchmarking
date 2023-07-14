# @lc app=leetcode id=2556 lang=python3
from typing import List

class Solution:
    def dfs(self, grid: List[List[int]], visited: List[List[bool]], row: int, col: int) -> None:
        m, n = len(grid), len(grid[0])
        
        if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or grid[row][col] == 0:
            return
        
        visited[row][col] = True
        
        self.dfs(grid, visited, row + 1, col)
        self.dfs(grid, visited, row, col + 1)
        
        
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        visited = [[False] * n for _ in range(m)]
        
        self.dfs(grid, visited, 0, 0)
        
        if visited[m - 1][n - 1]:
            return False
        
        for row in range(m):
            for col in range(n):
                grid[row][col] = 1 - grid[row][col]
                
                visited = [[False] * n for _ in range(m)]
                
                self.dfs(grid, visited, 0, 0)
                
                if not visited[m - 1][n - 1]:
                    return True
                
                grid[row][col] = 1 - grid[row][col]
                
        return False