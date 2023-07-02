# @lc app=leetcode id=1383 lang=python3
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = sorted(zip(efficiency, speed), reverse=True)
        max_performance = total_speed = 0
        pq = []

        for eff, spd in engineers:
            total_speed += spd
            heapq.heappush(pq, spd)

            if len(pq) > k:
                total_speed -= heapq.heappop(pq)

            performance = total_speed * eff
            max_performance = max(max_performance, performance)

        return max_performance % (10**9 + 7)