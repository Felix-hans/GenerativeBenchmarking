# @lc app=leetcode id=2556 lang=python
from typing import List

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        def dfs(row, col, grid):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True

            grid[row][col] = -1 # mark the cell as visited

            directions = [(1, 0), (0, 1)]
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if new_row < len(grid) and new_col < len(grid[0]) and grid[new_row][new_col] in [1, -1]:
                    if dfs(new_row, new_col, grid):
                        return True

            return False
        
        if not dfs(0, 0, grid):
            return True

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0

                    if not dfs(0, 0, grid):
                        return True

                    grid[i][j] = 1

        return False