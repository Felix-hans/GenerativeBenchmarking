# @lc app=leetcode id=587 lang=python3
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def distance(p: List[int], q: List[int]) -> int:
            return (q[1] - p[1]) ** 2 + (q[0] - p[0]) ** 2

        def next_to_top(stack: List[List[int]]) -> List[int]:
            return stack[-2]

        n = len(trees)
        if n <= 3:
            return trees

        trees.sort(key=lambda x: (x[0], x[1]))

        hull = []
        p = 0
        q = 0

        leftmost = trees[0]
        for i in range(1, n):
            if trees[i][0] < leftmost[0]:
                leftmost = trees[i]
                p = i

        while True:
            hull.append(trees[p])
            q = (p + 1) % n

            for i in range(n):
                if orientation(trees[p], trees[i], trees[q]) < 0:
                    q = i

            for i in range(n):
                if (
                    orientation(trees[p], trees[i], trees[q]) == 0
                    and distance(trees[p], trees[i]) > 0
                ):
                    hull.append(trees[i])

            p = q

            if p == 0:
                break

        return hull