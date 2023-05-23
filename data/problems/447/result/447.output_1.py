# @lc app=leetcode id=447 lang=python3
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomerangs = 0

        for i in range(len(points)):
            distances = {}
            for j in range(len(points)):
                if i != j:
                    distance = self.calculateDistance(points[i], points[j])
                    if distance in distances:
                        distances[distance] += 1
                    else:
                        distances[distance] = 1

            for distance_count in distances.values():
                boomerangs += distance_count * (distance_count - 1)

        return boomerangs

    def calculateDistance(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return (x2 - x1) ** 2 + (y2 - y1) ** 2