# @lc app=leetcode id=1383 lang=python3
from typing import List

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(speed, efficiency)
        engineers = sorted(engineers, key=lambda x: x[1], reverse=True)
        
        max_performance = 0
        total_speed = 0
        min_efficiency = float('inf')
        heap = []
        
        for spd, eff in engineers:
            if len(heap) >= k:
                total_speed -= heapq.heappop(heap)
            
            total_speed += spd
            
            heapq.heappush(heap, spd)
            
            min_efficiency = min(min_efficiency, eff)
            
            performance = total_speed * min_efficiency
            
            max_performance = max(max_performance, performance)
        
        return max_performance % (10**9 + 7)