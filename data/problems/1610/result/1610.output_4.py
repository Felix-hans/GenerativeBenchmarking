# @lc app=leetcode id=1610 lang=python3
import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same_location = 0
        max_points = 0

        for point in points:
            x, y = point
            if x == location[0] and y == location[1]:
                same_location += 1
            else:
                angles.append(math.atan2(y - location[1], x - location[0]))

        angles.sort()
        angles += [angle + 2 * math.pi] * len(angles)

        for i in range(len(angles)):
            current_points = same_location

            for j in range(i + 1, len(angles)):
                if angles[j] - angles[i] <= math.radians(angle):
                    current_points += 1
                else:
                    break

            max_points = max(max_points, current_points)

        return max_points