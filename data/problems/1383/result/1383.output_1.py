# @lc app=leetcode id=1383 lang=python3
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)  # Sort engineers by efficiency (descending order)
        speed_heap = []
        total_speed = 0
        max_performance = 0

        for curr_efficiency, curr_speed in engineers:
            total_speed += curr_speed
            heapq.heappush(speed_heap, curr_speed)

            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)

            performance = total_speed * curr_efficiency
            max_performance = max(max_performance, performance)

        return max_performance % (10**9 + 7)