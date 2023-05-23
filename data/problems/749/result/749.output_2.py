# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        while True:
            regions = self.get_viral_regions(isInfected)
            if not regions:
                break

            quarantine_region = max(regions, key=lambda r: r['uninfected']) # Select region with the most uninfected cells
            walls += self.quarantine_region(isInfected, quarantine_region)

            self.spread_virus(isInfected) # Spread the virus to neighboring cells

        return walls

    def get_viral_regions(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        visited = set()
        regions = []

        def bfs(i, j):
            queue = [(i, j)]
            region = {'infected': set([(i, j)]), 'uninfected': 0, 'boundary': set()}

            while queue:
                x, y = queue.pop(0)
                visited.add((x, y))

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if isInfected[nx][ny] == 1:
                            queue.append((nx, ny))
                            region['infected'].add((nx, ny))
                            visited.add((nx, ny))
                        else:
                            region['uninfected'] += 1
                            if isInfected[x][y] == 1:
                                region['boundary'].add((x, y))

            return region

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and isInfected[i][j] == 1:
                    regions.append(bfs(i, j))

        return regions

    def quarantine_region(self, isInfected, region):
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        for i, j in region['boundary']:
            isInfected[i][j] = -1 # Mark the boundary cells as quarantined
            walls += 1

        return walls

    def spread_virus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])
        infected = set()

        def bfs(i, j):
            queue = [(i, j)]

            while queue:
                x, y = queue.pop(0)

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and isInfected[nx][ny] == 0:
                        isInfected[nx][ny] = 1 # Spread the virus to neighboring cells
                        infected.add((nx, ny))
                        queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == -1:
                    bfs(i, j)

        for i