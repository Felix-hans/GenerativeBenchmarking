# @lc app=leetcode id=587 lang=python3
class Solution:
    def outerTrees(self, trees):
        def orientation(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def distance(p, q):
            return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

        def next_to_top(stack):
            return stack[-2]

        trees.sort(key=lambda p: (p[0], p[1]))

        n = len(trees)
        if n <= 2:
            return trees

        stack = []
        p0 = trees[0]  # The leftmost tree

        p1 = trees[1]
        i = 2
        while i < n:
            if orientation(p0, p1, trees[i]) != 0:
                break
            i += 1

        stack.append(p0)
        stack.append(p1)

        for j in range(i, n):
            while len(stack) >= 2 and orientation(next_to_top(stack), stack[-1], trees[j]) > 0:
                stack.pop()  # Remove points that make a clockwise turn

            stack.append(trees[j])

        max_x = max(trees, key=lambda p: p[0])

        upper = []
        for tree in trees:
            if tree != max_x and orientation(max_x, stack[-1], tree) == 0:
                upper.append(tree)

        stack.reverse()

        lower = []
        for tree in trees:
            if tree != max_x and orientation(max_x, stack[-1], tree) == 0:
                lower.append(tree)

        result = set(map(tuple, stack + upper + lower))

        return list(result)