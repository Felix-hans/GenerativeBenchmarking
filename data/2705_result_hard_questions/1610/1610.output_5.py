# @lc app=leetcode id=1610 lang=python3
from typing import List
from math import atan2, degrees

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        overlap = 0
        
        for point in points:
            x, y = point
            if x == location[0] and y == location[1]:
                overlap += 1
                continue
            angles.append(degrees(atan2(y - location[1], x - location[0])))
        
        angles.sort()
        n = len(angles)
        
        angles += [angle + angle_val for angle_val in angles]
        
        max_points = 0
        
        start = 0
        for end in range(n * 2):
            while angles[end] - angles[start] > angle:
                start += 1
            max_points = max(max_points, end - start + 1)
        
        return max_points + overlap