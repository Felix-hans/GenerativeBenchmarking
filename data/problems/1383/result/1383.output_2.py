# @lc app=leetcode id=1383 lang=python3
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency, speed)  # Combine efficiency and speed of engineers
        engineers = sorted(engineers, reverse=True)  # Sort engineers by decreasing efficiency

        speed_sum = 0
        performance = 0
        min_heap = []

        for eff, spd in engineers:
            heapq.heappush(min_heap, spd)  # Add the current engineer's speed to the min heap
            speed_sum += spd

            if len(min_heap) > k:
                speed_sum -= heapq.heappop(min_heap)  # Remove the engineer with the minimum speed

            performance = max(performance, speed_sum * eff)  # Calculate the current performance

        return performance % (10**9 + 7)