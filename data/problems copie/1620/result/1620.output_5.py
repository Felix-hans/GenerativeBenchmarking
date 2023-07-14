# @lc app=leetcode id=1620 lang=python3
from typing import List

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = 0
        best_coordinate = [0, 0]

        for x in range(51):
            for y in range(51):
                network_quality = 0

                for tower in towers:
                    tx, ty, tq = tower
                    distance = ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5

                    if distance <= radius:
                        signal_quality = tq // (1 + distance)
                        network_quality += signal_quality

                if network_quality > max_quality:
                    max_quality = network_quality
                    best_coordinate = [x, y]
                elif network_quality == max_quality:
                    if (x < best_coordinate[0]) or (x == best_coordinate[0] and y < best_coordinate[1]):
                        best_coordinate = [x, y]

        return best_coordinate