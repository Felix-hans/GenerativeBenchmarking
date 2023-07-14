# @lc app=leetcode id=2146 lang=python3
from typing import List
import heapq

class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        low, high = pricing
        pq = [(0, 0, start[0], start[1])]  # (distance, price, row, col)
        dist = [[float('inf')] * n for _ in range(m)]

        while pq and len(result) < k:
            _, price, row, col = heapq.heappop(pq)
            if low <= price <= high:
                result.append([row, col])

            if len(result) == k:
                break

            neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for nr, nc in neighbors:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                    distance = dist[row][col] + 1  # 1 step to move
                    if distance < dist[nr][nc]:
                        dist[nr][nc] = distance
                        heapq.heappush(pq, (distance, grid[nr][nc], nr, nc))

        return result