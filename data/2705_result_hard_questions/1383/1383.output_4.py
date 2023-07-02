# @lc app=leetcode id=1383 lang=python3
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(speed, efficiency))
        
        engineers.sort(key=lambda x: x[1], reverse=True)
        
        speed_heap = []
        
        total_speed = 0
        max_performance = 0
        
        for engineer_speed, engineer_efficiency in engineers:
            total_speed += engineer_speed
            
            heapq.heappush(speed_heap, engineer_speed)
            
            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)
            
            performance = total_speed * engineer_efficiency
            
            max_performance = max(max_performance, performance)
        
        return max_performance % (10**9 + 7)