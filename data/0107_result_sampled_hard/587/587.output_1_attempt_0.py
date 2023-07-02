# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else 2

        def next_to_top(stack):
            return stack[-2]

        n = len(trees)
        if n <= 3:
            return trees

        ymin = trees[0][1]
        min_idx = 0
        for i in range(1, n):
            y = trees[i][1]
            if (y < ymin) or (ymin == y and trees[i][0] < trees[min_idx][0]):
                ymin = y
                min_idx = i

        trees[0], trees[min_idx] = trees[min_idx], trees[0]

        p0 = trees[0]
        trees.sort(key=lambda p: (p[1] - p0[1], p0[0] - p[0]))

        m = 1  # Number of valid points
        for i in range(1, n):
            while i < n - 1 and orientation(p0, trees[i], trees[i + 1]) == 0:
                i += 1
            trees[m] = trees[i]
            m += 1

        if m <= 2:
            return trees[:m]

        stack = [trees[0], trees[1], trees[2]]
        for i in range(3, m):
            while len(stack) > 1 and orientation(next_to_top(stack), stack[-1], trees[i]) != 2:
                stack.pop()
            stack.append(trees[i])

        return stack