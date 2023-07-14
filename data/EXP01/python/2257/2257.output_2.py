# @lc app=leetcode id=2257 lang=python3
from typing import List
from collections import deque

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        for wall in walls:
            row, col = wall
            grid[row][col] = -1
        
        for guard in guards:
            row, col = guard
            queue = deque([(row, col)])
            visited = set([(row, col)])
            
            while queue:
                curr_row, curr_col = queue.popleft()
                grid[curr_row][curr_col] = 1
                
                for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_row, new_col = curr_row + d_row, curr_col + d_col
                    
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
        
        unguarded_count = sum(row.count(0) for row in grid)
        
        return unguarded_count