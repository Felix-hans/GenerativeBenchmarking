# @lc app=leetcode id=447 lang=python3
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0
        
        for i in range(len(points)):
            distances = {}  # Dictionary to store count of distances
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                distance = self.calculateDistance(points[i], points[j])
                distances[distance] = distances.get(distance, 0) + 1
                
            for count in distances.values():
                boomerangs += count * (count - 1)  # Count possible boomerangs for each distance
        
        return boomerangs

    def calculateDistance(self, point1: List[int], point2: List[int]) -> int:
        x1, y1 = point1
        x2, y2 = point2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2