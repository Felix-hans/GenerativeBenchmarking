# @lc app=leetcode id=1610 lang=python3
from math import atan2, degrees
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        angles = []
        same_point_count = 0
        loc_x, loc_y = location
        
        for x, y in points:
            if x == loc_x and y == loc_y:
                same_point_count += 1
            else:
                angles.append(degrees(atan2(y - loc_y, x - loc_x)))
        
        angles.sort()
        max_points = 0
        
        for i in range(len(angles)):
            angles.append(angles[i] + 360)  # Add rotated angles
        
        left = 0
        for right in range(len(angles)):
            while angles[right] - angles[left] > angle:
                left += 1
            max_points = max(max_points, right - left + 1)
        
        return max_points + same_point_count