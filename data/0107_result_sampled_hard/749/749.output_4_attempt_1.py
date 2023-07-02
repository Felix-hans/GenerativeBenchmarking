# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        visited = set()
        walls_built = 0
        iteration = 0
        
        def dfs(row, col):
            infected_count = 0
            boundary = set()
            stack = [(row, col)]
            
            while stack:
                r, c = stack.pop()
                if (r, c) in visited:
                    continue
                
                visited.add((r, c))
                
                if isInfected[r][c] == 0:
                    infected_count += 1
                    boundary.add((r, c))
                    continue
                
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                        stack.append((nr, nc))
            
            return infected_count, boundary
        
        def build_walls(region):
            for r, c in region:
                isInfected[r][c] = -1  # Mark the cell as a wall
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if 0 <= nr < m and 0 <= nc < n and isInfected[nr][nc] == 0:
                        isInfected[nr][nc] = 1  # Infect the cell for the next iteration
        
        while True:
            threatened_regions = []
            
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        infected_count, boundary = dfs(i, j)
                        threatened_regions.append((infected_count, boundary))
            
            if not threatened_regions:
                break
            
            threatened_regions.sort(reverse=True)  # Sort in descending order based on threat level
            
            most_threatened = threatened_regions[0]
            build_walls(most_threatened[1])
            walls_built += len(most_threatened[1])
            
            for region in threatened_regions[1:]:
                for r, c in region[1]:
                    if isInfected[r][c] == 1:
                        build_walls(dfs(r, c)[1])
            
            iteration += 1
        
        return walls_built