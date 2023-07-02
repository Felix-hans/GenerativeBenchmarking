# @lc app=leetcode id=1383 lang=python3
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)  # Sort engineers by efficiency in descending order
        max_performance = 0
        total_speed = 0
        speed_heap = []

        for eff, spd in engineers:
            total_speed += spd
            heapq.heappush(speed_heap, spd)

            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)

            performance = total_speed * eff
            max_performance = max(max_performance, performance)

        return max_performance % (10**9 + 7)