# @lc app=leetcode id=1383 lang=python3
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(s, e) for s, e in zip(speed, efficiency)]

        engineers.sort(key=lambda x: x[1], reverse=True)

        speed_sum = 0  # Running sum of speeds
        performance = 0  # Maximum performance

        speed_heap = []

        for engineer in engineers:
            speed_sum += engineer[0]

            heappush(speed_heap, engineer[0])

            if len(speed_heap) > k:
                min_speed = heappop(speed_heap)
                speed_sum -= min_speed

            performance = max(performance, speed_sum * engineer[1])

        return performance % (10**9 + 7)