# @lc app=leetcode id=447 lang=python3
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        
        for i in range(len(points)):
            distances = {}
            
            for j in range(len(points)):
                if i != j:
                    distance = self.calculateDistance(points[i], points[j])
                    if distance in distances:
                        distances[distance] += 1
                    else:
                        distances[distance] = 1
            
            for distance in distances.values():
                count += distance * (distance - 1)
        
        return count
    
    def calculateDistance(self, point1: List[int], point2: List[int]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return (x1 - x2) ** 2 + (y1 - y2) ** 2