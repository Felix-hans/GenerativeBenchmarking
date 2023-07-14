# @lc app=leetcode id=587 lang=python3
class Solution:
    def orientation(self, p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2
    
    def outerTrees(self, trees):
        n = len(trees)
        if n <= 3:
            return trees
        
        leftmost = min(trees, key=lambda x: x[0])
        hull = []
        p = leftmost
        q = None
        
        while True:
            hull.append(p)
            q = (p[0] + 1, p[1])  # Initialize q with a point not equal to p
            
            for i in range(n):
                if p == trees[i]:
                    continue
                if self.orientation(p, q, trees[i]) == 2:
                    q = trees[i]
            
            if q == leftmost:
                break
            
            p = q
        
        return hull