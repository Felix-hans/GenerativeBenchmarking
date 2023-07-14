# @lc app=leetcode id=2257 lang=python
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for r, c in guards:
            grid[r][c] = 1
        
        for r, c in walls:
            grid[r][c] = -1
        
        unguarded = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded += 1
        
        return unguarded