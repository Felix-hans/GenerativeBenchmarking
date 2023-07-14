# @lc app=leetcode id=2556 lang=python3
class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return True
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != 1:
                return False
            
            grid[row][col] = -1  # Mark cell as visited
            
            if dfs(row + 1, col) or dfs(row, col + 1):
                return True
            
            grid[row][col] = 1  # Reset cell
            
            return False
        
        if not dfs(0, 0):  # Check if there is a path without flipping any cells
            return True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    grid[i][j] = 1  # Flip cell
                    
                    if not dfs(0, 0):  # Check if path is disconnected after flipping cell
                        return True
                    
                    grid[i][j] = 0  # Reset cell
        
        return False