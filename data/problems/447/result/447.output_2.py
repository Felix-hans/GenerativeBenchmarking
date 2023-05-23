# @lc app=leetcode id=447 lang=python3
from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def calculate_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return (x2 - x1) ** 2 + (y2 - y1) ** 2

        num_boomerangs = 0

        for i, p1 in enumerate(points):
            distances = defaultdict(int)
            for j, p2 in enumerate(points):
                if i != j:
                    distance = calculate_distance(p1, p2)
                    distances[distance] += 1

            for count in distances.values():
                num_boomerangs += count * (count - 1)

        return num_boomerangs