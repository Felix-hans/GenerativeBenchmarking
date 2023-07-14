# @lc app=leetcode id=2257 lang=python
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[False] * n for _ in range(m)]
        
        for guard in guards:
            row, col = guard[0], guard[1]
            for i in range(row+1, m):
                if grid[i][col]:
                    break
                grid[i][col] = True
            for i in range(row-1, -1, -1):
                if grid[i][col]:
                    break
                grid[i][col] = True
            for j in range(col+1, n):
                if grid[row][j]:
                    break
                grid[row][j] = True
            for j in range(col-1, -1, -1):
                if grid[row][j]:
                    break
                grid[row][j] = True
        
        for wall in walls:
            row, col = wall[0], wall[1]
            grid[row][col] = True
        
        count = 0
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    count += 1
        
        return count