# @lc app=leetcode id=2556 lang=python3
from typing import List, Tuple


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        def bfs(grid: List[List[int]]) -> bool:
            visited = [[False for _ in range(n)] for _ in range(m)]
            queue = [(0, 0)]
            
            while queue:
                row, col = queue.pop(0)
                if row == m-1 and col == n-1:
                    return True
                
                if grid[row][col] == 1:
                    if row+1 < m and not visited[row+1][col]:
                        queue.append((row+1, col))
                        visited[row+1][col] = True
                    if col+1 < n and not visited[row][col+1]:
                        queue.append((row, col+1))
                        visited[row][col+1] = True
            
            return False
        
        
        if not bfs(grid):
            return True
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    if not bfs(grid):
                        return True
                    grid[row][col] = 1
                
        return False


grid = [
    [1, 1, 1],
    [1, 0, 0],
    [1, 1, 1]
]
solution = Solution()
print(solution.isPossibleToCutPath(grid))  # Output: True