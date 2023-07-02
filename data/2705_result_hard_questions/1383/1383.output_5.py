# @lc app=leetcode id=1383 lang=python3
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        speed_heap = []
        total_speed = 0
        result = 0

        for curr_speed, curr_efficiency in engineers:
            total_speed += curr_speed
            heapq.heappush(speed_heap, curr_speed)

            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)

            curr_performance = total_speed * curr_efficiency
            result = max(result, curr_performance)

        return result % (10**9 + 7)