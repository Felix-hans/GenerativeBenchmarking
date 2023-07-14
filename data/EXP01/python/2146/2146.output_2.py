# @lc app=leetcode id=2146 lang=python3
import heapq
from typing import List

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        low, high = pricing

        pq = []
        heapq.heappush(pq, (0, low, start[0], start[1]))
        
        visited = set()
        
        results = []
        
        while pq and len(results) < k:
            dist, price, row, col = heapq.heappop(pq)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            if low <= grid[row][col] <= high:
                results.append([row, col])
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                    new_dist = dist + 1
                    new_price = min(price, grid[new_row][new_col])
                    heapq.heappush(pq, (new_dist, new_price, new_row, new_col))
        
        return results