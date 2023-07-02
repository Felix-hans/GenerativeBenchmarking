# @lc app=leetcode id=1610 lang=python3
from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same_location_count = 0

        for point in points:
            x, y = point[0] - location[0], point[1] - location[1]
            if x == 0 and y == 0:
                same_location_count += 1
            else:
                angles.append(math.atan2(y, x) * 180 / math.pi)

        angles.sort()
        angles += [angle + angle_i for angle_i in angles]

        max_visible = 0
        start = 0

        for end in range(len(angles)):
            while angles[end] - angles[start] > angle:
                start += 1
            max_visible = max(max_visible, end - start + 1)

        return max_visible + same_location_count