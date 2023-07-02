# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def next_to_top(stack):
            return stack[-2]

        def distance(p, q):
            return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2

        trees.sort(key=lambda x: (x[0], x[1]))

        n = len(trees)
        if n <= 1:
            return trees

        hull = []
        p = 0
        q = 0

        while True:
            hull.append(trees[p])
            q = (p + 1) % n

            for i in range(n):
                if orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i

            for i in range(n):
                if i != p and i != q and orientation(trees[p], trees[i], trees[q]) == 0 and distance(trees[p], trees[i]) > distance(trees[p], trees[q]):
                    q = i

            p = q

            if p == 0:
                break

        return hull