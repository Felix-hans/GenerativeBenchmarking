# @lc app=leetcode id=1610 lang=python3
import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same_point_count = 0

        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            angle_rad = math.atan2(dy, dx)
            angles.append(math.degrees(angle_rad))
            if dx == 0 and dy == 0:
                same_point_count += 1

        angles.sort()

        max_points = 0

        for i in range(len(angles)):
            rotated_angles = angles[i:] + [angle + ang for ang in angles[:i]]
            current_points = 1

            for j in range(1, len(rotated_angles)):
                diff = rotated_angles[j] - rotated_angles[j - 1]
                if diff > angle:
                    current_points = 1
                else:
                    current_points += 1

                max_points = max(max_points, current_points)

        return max_points + same_point_count