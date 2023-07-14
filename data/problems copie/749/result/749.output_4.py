# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        def dfs(i, j):

            if i < 0 or i >= m or j < 0 or j >= n or isInfected[i][j] != 1:
                return 0

            isInfected[i][j] = -1

            count = 1  # Count the number of infected cells in the region

            count += dfs(i + 1, j)
            count += dfs(i - 1, j)
            count += dfs(i, j + 1)
            count += dfs(i, j - 1)

            return count

        def build_walls(i, j):

            if i < 0 or i >= m or j < 0 or j >= n or isInfected[i][j] != -1:
                return

            isInfected[i][j] = -2

            build_walls(i + 1, j)
            build_walls(i - 1, j)
            build_walls(i, j + 1)
            build_walls(i, j - 1)

        while True:
            regions = []  # List to store information about each infected region
            visited = [[False] * n for _ in range(m)]  # Visited matrix to track visited cells

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region_size = dfs(i, j)
                        regions.append((region_size, i, j))

            if not regions:
                return walls

            regions.sort(reverse=True)  # Sort regions in descending order of size
            region_size, i, j = regions[0]  # Select the region with the maximum size
            walls += build_walls(i, j)  # Build walls around the selected region

            infected_cells = []  # List to store information about newly infected cells
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        if i > 0 and isInfected[i - 1][j] == 0:
                            infected_cells.append((i - 1, j))
                        if i < m - 1 and isInfected[i + 1][j] == 0:
                            infected_cells.append((i + 1, j))
                        if j > 0 and isInfected[i][j - 1] == 0: