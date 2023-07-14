# @lc app=leetcode id=149 lang=python3
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        max_points = 0

        for i in range(len(points)):
            slopes = {}
            duplicate = 1
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue

                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)

                if slope not in slopes:
                    slopes[slope] = 1
                else:
                    slopes[slope] += 1

            current_max = duplicate
            if slopes:
                current_max = max(current_max, max(slopes.values()) + duplicate)

            max_points = max(max_points, current_max)

        return max_points