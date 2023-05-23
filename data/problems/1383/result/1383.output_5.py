# @lc app=leetcode id=1383 lang=python3
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = zip(efficiency, speed)  # Combine efficiency and speed
        engineers = sorted(engineers, reverse=True)  # Sort engineers by decreasing efficiency
        team_speeds = []
        total_speed = 0
        max_performance = 0

        for eff, spd in engineers:
            heapq.heappush(team_speeds, spd)  # Add current engineer's speed to the heap
            total_speed += spd

            if len(team_speeds) > k:
                total_speed -= heapq.heappop(team_speeds)  # Remove the engineer with the lowest speed

            performance = total_speed * eff  # Calculate current performance
            max_performance = max(max_performance, performance)

        return max_performance % (10 ** 9 + 7)