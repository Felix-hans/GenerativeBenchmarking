# @lc app=leetcode id=149 lang=python3
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        max_points = 0
        
        for i in range(len(points)):
            slopes = {}
            same_points = 1  # Count the same point
            
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    same_points += 1
                    continue
                
                if x1 == x2:  # Vertical line
                    slope = float('inf')
                else:
                    slope = (y2 - y1) / (x2 - x1)
                
                if slope not in slopes:
                    slopes[slope] = 1
                else:
                    slopes[slope] += 1
            
            max_points = max(max_points, same_points)
            if slopes:
                max_points = max(max_points, max(slopes.values()) + same_points)
        
        return max_points