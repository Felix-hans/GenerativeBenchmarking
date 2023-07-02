# @lc app=leetcode id=1610 lang=python3
from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        polar_points = []
        location_x, location_y = location[0], location[1]
        
        for point in points:
            point_x, point_y = point[0], point[1]
            dx, dy = point_x - location_x, point_y - location_y
            polar_angle = math.atan2(dy, dx) * (180 / math.pi)
            polar_points.append(polar_angle)
        
        polar_points.sort()
        polar_points += [angle + angle for angle in polar_points]
        
        max_points_seen = 0
        current_points_seen = 0
        start_index = 0
        
        for i in range(len(polar_points)):
            current_points_seen += 1
            
            while polar_points[i] - polar_points[start_index] > angle:
                current_points_seen -= 1
                start_index += 1
            
            max_points_seen = max(max_points_seen, current_points_seen)
        
        return max_points_seen