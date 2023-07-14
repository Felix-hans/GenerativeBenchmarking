# @lc app=leetcode id=2146 lang=python3
import heapq

class Solution:
    def highestRankedKItems(self, grid, pricing, start, k):
        m = len(grid)
        n = len(grid[0])
        
        distance = [[float('inf')] * n for _ in range(m)]
        price = [[0] * n for _ in range(m)]
        row = [[0] * n for _ in range(m)]
        col = [[0] * n for _ in range(m)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        queue = []
        heapq.heappush(queue, (0, pricing[0], start[0], start[1]))
        
        while queue:
            curr_dist, curr_price, curr_row, curr_col = heapq.heappop(queue)
            
            if distance[curr_row][curr_col] < curr_dist:
                continue
            
            distance[curr_row][curr_col] = curr_dist
            price[curr_row][curr_col] = curr_price
            row[curr_row][curr_col] = curr_row
            col[curr_row][curr_col] = curr_col
            
            for direction in directions:
                next_row = curr_row + direction[0]
                next_col = curr_col + direction[1]
                
                if 0 <= next_row < m and 0 <= next_col < n:
                    next_dist = curr_dist + 1
                    next_price = max(curr_price, grid[next_row][next_col])
                    
                    if next_dist < distance[next_row][next_col]:
                        heapq.heappush(queue, (next_dist, next_price, next_row, next_col))
        
        items = []
        
        for i in range(m):
            for j in range(n):
                curr_price = price[i][j]
                
                if pricing[0] <= curr_price <= pricing[1]:
                    items.append((distance[i][j], curr_price, row[i][j], col[i][j]))
        
        items.sort(reverse=True)
        
        top_items = [[item[2], item[3]] for item in items[:k]]
        
        return top_items