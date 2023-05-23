# @lc app=leetcode id=1610 lang=python3
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        x, y = location
        same_location_count = 0

        for xi, yi in points:
            if xi == x and yi == y:
                same_location_count += 1
            else:
                angles.append(math.atan2(yi - y, xi - x) * 180 / math.pi)

        angles.sort()
        angles += [angle + angle for angle in angles]

        start, end = 0, 0
        max_visible = 0
        n = len(angles)

        while start < n:
            while angles[end] - angles[start] <= angle:
                end += 1

            max_visible = max(max_visible, end - start)
            start += 1

        return max_visible + same_location_count