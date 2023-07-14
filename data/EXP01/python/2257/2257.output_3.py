# @lc app=leetcode id=2257 lang=python3
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)] # create a grid of size m x n
        
        for guard in guards:
            x, y = guard
            grid[x][y] = 1
        
        for wall in walls:
            x, y = wall
            grid[x][y] = -1
        
        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    count += 1
        
        return count