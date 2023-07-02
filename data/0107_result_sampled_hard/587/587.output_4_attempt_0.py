# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # Collinear
            elif val > 0:
                return 1  # Clockwise
            else:
                return 2  # Counterclockwise

        def next_to_top(stack):
            return stack[-2]

        trees.sort(key=lambda x: (x[0], x[1]))

        n = len(trees)
        if n <= 1:
            return trees

        hull = []

        leftmost = 0
        for i in range(1, n):
            if trees[i][0] < trees[leftmost][0]:
                leftmost = i

        p = leftmost
        q = 0
        while True:
            hull.append(trees[p])
            q = (p + 1) % n

            for i in range(n):
                if orientation(trees[p], trees[i], trees[q]) == 2:
                    q = i

            p = q

            if p == leftmost:
                break

        return hull