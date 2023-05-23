# @lc app=leetcode id=149 lang=python3
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        max_points = 0
        for i in range(len(points)):
            slopes = {}  # Dictionary to store the count of points with the same slope
            duplicates = 1  # Count of duplicate points

            for j in range(len(points)):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif x1 == x2:
                    slope = float('inf')  # Vertical line, slope is infinity
                    slopes[slope] = slopes.get(slope, 0) + 1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    slopes[slope] = slopes.get(slope, 0) + 1

            max_points = max(max_points, duplicates + max(slopes.values(), default=0))

        return max_points