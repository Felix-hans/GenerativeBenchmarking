# @lc app=leetcode id=1610 lang=python3
from typing import List
import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        polar_points = []
        location_x, location_y = location[0], location[1]
        same_location = 0  # Number of points at the same location as the given location
        
        for point in points:
            point_x, point_y = point[0], point[1]
            dx, dy = point_x - location_x, point_y - location_y
            
            if dx == 0 and dy == 0:
                same_location += 1
                continue
            
            polar_angle = math.atan2(dy, dx) * (180 / math.pi)
            polar_points.append(polar_angle)
            polar_points.append(polar_angle + 360)  # Consider both positive and negative angles
        
        polar_points.sort()
        
        max_points_seen = 0
        current_points_seen = 0
        start_index = 0
        
        for i in range(len(polar_points)):
            current_points_seen += 1
            
            while polar_points[i] - polar_points[start_index] > angle:
                current_points_seen -= 1
                start_index += 1
            
            max_points_seen = max(max_points_seen, current_points_seen)
        
        return max_points_seen + same_location