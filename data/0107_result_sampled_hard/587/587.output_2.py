# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def orientation(self, p: List[int], q: List[int], r: List[int]) -> int:
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n <= 3:
            return trees

        bottom_left = min(trees, key=lambda t: (t[1], t[0]))

        trees.sort(key=lambda t: (self.orientation(bottom_left, t, [bottom_left[0] + 1, bottom_left[1]]), -t[1], t[0]))

        hull = [trees[0], trees[1]]
        for i in range(2, n):
            while len(hull) >= 2 and self.orientation(hull[-2], hull[-1], trees[i]) <= 0:
                hull.pop()
            hull.append(trees[i])

        return hull