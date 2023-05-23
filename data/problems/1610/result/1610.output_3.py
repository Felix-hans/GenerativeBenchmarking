# @lc app=leetcode id=1610 lang=python3
from math import atan2, degrees
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        num_points_at_location = 0
        max_visible_points = 0

        for point in points:
            if point == location:
                num_points_at_location += 1
            else:
                x, y = point[0] - location[0], point[1] - location[1]
                angle = degrees(atan2(y, x))
                angles.append(angle)

        angles.sort()
        angles += [angle + 360 for angle in angles]  # Duplicate angles for circular cases

        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_visible_points = max(max_visible_points, right - left + 1)

        return max_visible_points + num_points_at_location