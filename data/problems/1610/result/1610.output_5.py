# @lc app=leetcode id=1610 lang=python3
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        def calculate_angle(x, y):
            dx = x - location[0]
            dy = y - location[1]
            return math.atan2(dy, dx) * (180 / math.pi)

        polar_points = []
        max_points = 0
        same_location = 0

        for point in points:
            x, y = point
            if x == location[0] and y == location[1]:
                same_location += 1
            else:
                polar_points.append(calculate_angle(x, y))

        polar_points.sort()
        polar_points += [angle + polar_point for polar_point in polar_points]

        start = 0
        for end in range(len(polar_points)):
            while polar_points[end] - polar_points[start] > angle:
                start += 1
            max_points = max(max_points, end - start + 1)

        return max_points + same_location