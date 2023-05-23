# @lc app=leetcode id=1266 lang=python3
import math

class Solution:
    def minTimeToVisitAllPoints(self, points):
        total_time = 0
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            diagonal_distance = min(dx, dy)
            
            remaining_distance = max(dx, dy) - diagonal_distance
            
            time = diagonal_distance * math.sqrt(2) + remaining_distance
            
            total_time += time
        
        return int(total_time)