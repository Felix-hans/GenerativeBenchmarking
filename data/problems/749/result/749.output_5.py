# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls_built = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(row, col):
            if isInfected[row][col] == -1:
                return 0
            
            infected_cells = 0
            perimeter = 0
            walls = 0
            isInfected[row][col] = -1  # Mark the cell as visited
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < m and 0 <= new_col < n:
                    if isInfected[new_row][new_col] == 1:
                        perimeter += 1
                        infected_cells += dfs(new_row, new_col)
                    elif isInfected[new_row][new_col] == 0:
                        walls += 1
            
            if walls > 0:
                walls_built += walls
                infected_cells += perimeter
            
            return infected_cells
        
        while True:
            regions = []
            visited = set()
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region = []
                        perimeter = dfs(i, j)
                        regions.append((region, perimeter))
                        visited.update(region)
            
            if not regions:
                break
            
            regions.sort(key=lambda x: x[1], reverse=True)
            
            for region, _ in regions[0][0]:
                isInfected[region[0]][region[1]] = -1
        
            for region, _ in regions[1:]:
                for row, col in region:
                    for dx, dy in directions:
                        new_row, new_col = row + dx, col + dy
                        if 0 <= new_row < m and 0 <= new_col < n and isInfected[new_row][new_col] == 0:
                            isInfected[new_row][new_col] = 1
        
        return walls_built