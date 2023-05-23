# @lc app=leetcode id=149 lang=python3
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        max_points_on_line = 0
        
        for i in range(len(points)):
            slopes = {}
            same_point_count = 1
            
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    same_point_count += 1
                elif x1 == x2:
                    slope = float('inf')
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
            
            max_points_on_line = max(max_points_on_line, same_point_count)
            for slope_count in slopes.values():
                max_points_on_line = max(max_points_on_line, same_point_count + slope_count)
        
        return max_points_on_line