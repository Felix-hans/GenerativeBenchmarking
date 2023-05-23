# @lc app=leetcode id=1620 lang=python3
from typing import List
import math

class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_quality = 0
        cx, cy = -1, -1

        for x in range(51):
            for y in range(51):
                total_quality = 0

                for tower in towers:
                    xi, yi, qi = tower
                    d = math.sqrt((x - xi) ** 2 + (y - yi) ** 2)

                    if d <= radius:
                        signal = math.floor(qi / (1 + d))
                        total_quality += signal

                if total_quality > max_quality or (total_quality == max_quality and (x, y) < (cx, cy)):
                    max_quality = total_quality
                    cx, cy = x, y

        return [cx, cy]