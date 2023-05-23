# @lc app=leetcode id=1620 lang=python3
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        def calculate_quality(x1, y1, quality, x2, y2):
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            return quality // (1 + distance)

        max_quality = 0
        best_coordinate = None

        for x in range(51):
            for y in range(51):
                network_quality = 0
                for tower in towers:
                    tower_x, tower_y, quality = tower
                    if ((tower_x - x) ** 2 + (tower_y - y) ** 2) ** 0.5 <= radius:
                        network_quality += calculate_quality(tower_x, tower_y, quality, x, y)

                if network_quality > max_quality:
                    max_quality = network_quality
                    best_coordinate = [x, y]
                elif network_quality == max_quality:
                    if best_coordinate is None or (x < best_coordinate[0]) or (x == best_coordinate[0] and y < best_coordinate[1]):
                        best_coordinate = [x, y]

        return best_coordinate