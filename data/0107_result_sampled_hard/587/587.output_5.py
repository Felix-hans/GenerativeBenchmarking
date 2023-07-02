# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            elif val > 0:
                return 1
            else:
                return -1
        
        n = len(trees)
        if n <= 3:
            return trees
        
        leftmost = min(trees, key=lambda point: point[0])
        
        hull = []
        p = trees.index(leftmost)
        q = None
        
        while True:
            hull.append(trees[p])
            q = (p + 1) % n
            
            for r in range(n):
                if orientation(trees[p], trees[r], trees[q]) != -1:
                    q = r
                    
            p = q
            
            if p == 0:
                break
        
        return hull