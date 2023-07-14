# @lc app=leetcode id=2352 lang=python3
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        
        for ri in range(n):
            row = grid[ri]
            
            for cj in range(n):
                column = [grid[i][cj] for i in range(n)]
                
                if row == column:
                    count += 1
        
        return count