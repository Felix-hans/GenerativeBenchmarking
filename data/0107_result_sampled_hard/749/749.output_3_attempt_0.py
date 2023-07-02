# @lc app=leetcode id=749 lang=python3
class Solution:
    def containVirus(self, isInfected):
        def spread_virus(grid, row, col, visited):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 2
                or (row, col) in visited
            ):
                return 0
            
            if grid[row][col] == 0:
                grid[row][col] = 1
                visited.add((row, col))
                return 1 + (
                    spread_virus(grid, row + 1, col, visited)
                    + spread_virus(grid, row - 1, col