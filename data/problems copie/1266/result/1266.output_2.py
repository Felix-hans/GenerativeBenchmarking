# @lc app=leetcode id=1266 lang=python3
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i+1]
            
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            
            diagonal_time = min(dx, dy)
            
            remaining_time = max(dx, dy) - diagonal_time
            
            segment_time = diagonal_time * sqrt(2) + remaining_time
            
            total_time += segment_time
        
        return int(total_time)