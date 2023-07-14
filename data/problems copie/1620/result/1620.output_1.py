# @lc app=leetcode id=1620 lang=python3
import math
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def calculate_quality(tower, coord):
            x, y, q = tower
            d = math.sqrt((x - coord[0])**2 + (y - coord[1])**2)
            return q // (1 + d)

        max_quality = 0
        best_coordinate = [0, 0]

        for x in range(51):
            for y in range(51):
                network_quality = 0
                for tower in towers:
                    if math.sqrt((tower[0] - x)**2 + (tower[1] - y)**2) <= radius:
                        network_quality += calculate_quality(tower, (x, y))

                if network_quality > max_quality:
                    max_quality = network_quality
                    best_coordinate = [x, y]
                elif network_quality == max_quality and (x < best_coordinate[0] or (x == best_coordinate[0] and y < best_coordinate[1])):
                    best_coordinate = [x, y]

        return best_coordinate