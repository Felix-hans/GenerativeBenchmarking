# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        while True:
            regions = self.getRegions(isInfected)
            if not regions:
                break

            quarantined_region = max(regions, key=lambda x: x[2])
            walls += self.quarantineRegion(quarantined_region, isInfected)

            self.spreadVirus(isInfected)

        return walls

    def getRegions(self, isInfected: List[List[int]]) -> List[List[int]]:
        m, n = len(isInfected), len(isInfected[0])
        visited = set()
        regions = []

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if (
                i < 0 or i >= m or
                j < 0 or j >= n or
                isInfected[i][j] != 1 or
                (i, j) in visited
            ):
                return 0

            visited.add((i, j))
            size = 1
            perimeter = 0

            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if (
                    nx < 0 or nx >= m or
                    ny < 0 or ny >= n or
                    isInfected[nx][ny] == 2 or
                    (nx, ny) in visited
                ):
                    continue

                if isInfected[nx][ny] == 0:
                    perimeter += 1
                elif isInfected[nx][ny] == 1:
                    size += dfs(nx, ny)

            perimeter += size
            return size

        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == 1 and (i, j) not in visited:
                    size = dfs(i, j)
                    regions.append([i, j, size])

        return regions

    def quarantineRegion(self, region: List[int], isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0
        queue = [(region[0], region[1])]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            i, j = queue.pop(0)

            if isInfected[i][j] != 1:
                continue

            isInfected[i][j] = 2

            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if (
                    ni >= 0 and ni < m and
                    nj >= 0 and nj < n and
                    isInfected[ni][nj] == 1
                ):
                    queue.append((ni, nj))
                elif (
                    ni < 0 or ni >= m or
                    nj < 0 or nj >= n or
                    isInfected[ni][nj] == 0
                ):
                    walls += 1

        return walls

    def spreadVirus(self, isInfected: List[List[int]]) -> None:
        m, n = len(isInfected