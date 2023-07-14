# @lc app=leetcode id=2257 lang=python
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded_cells = set()
        
        for wall in walls:
            guarded_cells.add((wall[0], wall[1]))
            
        for guard in guards:
            guarded_cells.add((guard[0], guard[1]))
        
        unguarded_count = 0
        
        for i in range(m):
            for j in range(n):
                if (i, j) not in guarded_cells:
                    unguarded_count += 1
        
        return unguarded_count