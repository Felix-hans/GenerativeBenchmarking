# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def orientation(self, p: List[int], q: List[int], r: List[int]) -> int:
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n <= 3:
            return trees

        leftmost = min(trees, key=lambda t: t[0])

        hull = []
        p = leftmost
        while True:
            hull.append(p)
            q = (p[0] + 1, p[1])
            for r in trees:
                if r == p:
                    continue
                o = self.orientation(p, q, r)
                if o < 0 or (o == 0 and r[0] > q[0]):
                    q = r
            p = q
            if p == leftmost:
                break

        return hull