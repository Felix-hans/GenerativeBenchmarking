# @lc app=leetcode id=587 lang=python3
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees = sorted(set(map(tuple, trees)))

        def ccw(p1, p2, p3):
            return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])

        lower_hull = []
        for tree in trees:
            while len(lower_hull) >= 2 and ccw(lower_hull[-2], lower_hull[-1], tree) < 0:
                lower_hull.pop()
            lower_hull.append(tree)

        upper_hull = []
        for tree in reversed(trees):
            while len(upper_hull) >= 2 and ccw(upper_hull[-2], upper_hull[-1], tree) < 0:
                upper_hull.pop()
            upper_hull.append(tree)

        convex_hull = lower_hull[:-1] + upper_hull[:-1]

        return convex_hull