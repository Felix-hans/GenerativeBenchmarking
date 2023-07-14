# @lc app=leetcode id=1383 lang=python3
import heapq
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))  # Combine efficiency and speed into tuples
        engineers.sort(reverse=True)  # Sort engineers in descending order of efficiency

        max_performance = 0
        total_speed = 0
        heap = []
        for eff, spd in engineers:
            heapq.heappush(heap, spd)  # Add speed to the heap
            total_speed += spd

            if len(heap) > k:
                total_speed -= heapq.heappop(heap)  # Remove the engineer with the lowest speed

            max_performance = max(max_performance, total_speed * eff)

        return max_performance % (10**9 + 7)