# @lc app=leetcode id=587 lang=python3
from typing import List

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def orientation(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        
        leftmost = min(trees, key=lambda p: p[0])
        hull = []
        point_on_hull = leftmost

        while True:
            hull.append(point_on_hull)
            endpoint = trees[0]

            for i in range(1, len(trees)):
                if (endpoint == point_on_hull) or (orientation(point_on_hull, endpoint, trees[i]) < 0):
                    endpoint = trees[i]

            point_on_hull = endpoint

            if point_on_hull == leftmost:
                break

        return hull