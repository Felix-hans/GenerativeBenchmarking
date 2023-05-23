# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        while True:
            regions = self.get_infected_regions(isInfected)  # Get all infected regions

            if not regions:
                break  # No more infected regions, exit the loop

            max_threatened_cells = -1
            quarantine_region = None
            for region in regions:
                threatened_cells = self.get_threatened_cells(isInfected, region)
                if len(threatened_cells) > max_threatened_cells:
                    max_threatened_cells = len(threatened_cells)
                    quarantine_region = region

            self.add_walls(isInfected, quarantine_region)
            walls += self.count_walls(quarantine_region)

            self.spread_virus(isInfected)

        return walls

    def get_infected_regions(self, isInfected: List[List[int]]) -> List[List[tuple]]:
        m, n = len(isInfected), len(isInfected[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        regions = []

        def bfs(i, j):
            queue = [(i, j)]
            region = []
            while queue:
                x, y = queue.pop(0)
                if not visited[x][y]:
                    visited[x][y] = True
                    region.append((x, y))
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and isInfected[nx][ny] == 1:
                            queue.append((nx, ny))
            return region

        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == 1 and not visited[i][j]:
                    regions.append(bfs(i, j))

        return regions

    def get_threatened_cells(self, isInfected: List[List[int]], region: List[tuple]) -> set:
        m, n = len(isInfected), len(isInfected[0])
        threatened_cells = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for x, y in region:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 0:
                    threatened_cells.add((nx, ny))

        return threatened_cells

    def add_walls(self, isInfected: List[List[int]], region: List[tuple]) -> None:
        for x, y in region:
            isInfected[x][y] = -1

    def count_walls(self, region: List[tuple]) -> int:
        return len(region)

    def spread_virus(self, isInfected: List[List[int]]) -> None:
        m, n =