# @lc app=leetcode id=447 lang=python3
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        num_boomerangs = 0
        
        for i in range(len(points)):
            distances = {}  # Hashmap to store distances and their frequencies
            
            for j in range(len(points)):
                if i != j:
                    distance = (points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2
                    
                    distances[distance] = distances.get(distance, 0) + 1
            
            for freq in distances.values():
                num_boomerangs += freq * (freq - 1)  # Calculate permutations of 2 from freq
            
        return num_boomerangs