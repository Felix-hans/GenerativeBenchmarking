# @lc app=leetcode id=1610 lang=python3
from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        overlap = 0
        max_points = 0

        for point in points:
            x, y = point[0] - location[0], point[1] - location[1]
            if x == 0 and y == 0:
                overlap += 1
                continue
            angles.append(math.degrees(math.atan2(y, x)))

        angles.sort()

        angles += [angle + angle_i for angle_i in angles]

        for i in range(len(angles)):
            start = end = 0
            while angles[i] - angles[start] > angle / 2:
                start += 1
            while angles[i] - angles[end] >= -angle / 2:
                end += 1
            max_points = max(max_points, end - start)

        return max_points + overlap