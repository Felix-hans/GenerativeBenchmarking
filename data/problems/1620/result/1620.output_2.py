# @lc app=leetcode id=1620 lang=python3
import math
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = 0
        best_coordinate = [float('inf'), float('inf')]  # Initialize with a large coordinate
        
        for x in range(51):
            for y in range(51):
                quality = 0
                
                for tower in towers:
                    xi, yi, qi = tower
                    distance = math.sqrt((xi - x) ** 2 + (yi - y) ** 2)
                    
                    if distance <= radius:
                        quality += qi // (1 + distance)
                
                if quality > max_quality:
                    max_quality = quality
                    best_coordinate = [x, y]
                elif quality == max_quality:
                    best_coordinate = min(best_coordinate, [x, y])  # Update lexicographically minimum coordinate
        
        return best_coordinate