# @lc app=leetcode id=2257 lang=python3
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]  # Initialize the grid with all cells set to 0
        
        for guard in guards:
            self.markGuardedCells(grid, m, n, guard)  # Mark cells seen by guards
            
        for wall in walls:
            self.markGuardedCells(grid, m, n, wall)  # Mark cells corresponding to walls
            
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # Count unguarded cells
                    count += 1
                    
        return count
    
    def markGuardedCells(self, grid: List[List[int]], m: int, n: int, position: List[int]) -> None:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Cardinal directions
        
        for direction in directions:
            row, col = position
            
            while 0 <= row < m and 0 <= col < n and grid[row][col] != 1:  # Move in the current direction until we reach a wall or another guard
                grid[row][col] = 1
                row += direction[0]
                col += direction[1]