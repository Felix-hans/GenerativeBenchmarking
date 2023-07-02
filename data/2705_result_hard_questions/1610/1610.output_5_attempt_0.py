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
        angles += [angle + angle_val for angle_val in angles]
        
        start = 0
        current_points = 0
        max_points = 0
        
        for end in range(len(angles)):
            while angles[end] - angles[start] > angle:
                current_points -= 1
                start += 1
            
            current_points += 1
            max_points = max(max_points, current_points)
        
        return max_points + overlap