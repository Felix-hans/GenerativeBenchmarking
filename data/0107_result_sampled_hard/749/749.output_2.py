# @lc app=leetcode id=749 lang=python3
from typing import List


class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        def get_neighbors(row, col):
            neighbors = []
            if row > 0:
                neighbors.append((row - 1, col))
            if row < m - 1:
                neighbors.append((row + 1, col))
            if col > 0:
                neighbors.append((row, col - 1))
            if col < n - 1:
                neighbors.append((row, col + 1))
            return neighbors

        def dfs(row, col, visited, region_number, region, perimeter):
            visited.add((row, col))
            region.add((row, col))

            for nr, nc in get_neighbors(row, col):
                if isInfected[nr][nc] == 1 and (nr, nc) not in visited:
                    perimeter.add((nr, nc))
                    dfs(nr, nc, visited, region_number, region, perimeter)

        def build_walls(region):
            perimeter = set()
            for row, col in region:
                for nr, nc in get_neighbors(row, col):
                    if isInfected[nr][nc] == 0:
                        perimeter.add((nr, nc))
            return perimeter

        def spread_virus(region):
            for row, col in region:
                for nr, nc in get_neighbors(row, col):
                    if isInfected[nr][nc] == 0:
                        isInfected[nr][nc] = 1

        while True:
            regions = []
            visited = set()
            region_number = 2

            for row in range(m):
                for col in range(n):
                    if isInfected[row][col] == 1 and (row, col) not in visited:
                        region = set()
                        perimeter = set()
                        dfs(row, col, visited, region_number, region, perimeter)
                        regions.append((region_number, region, perimeter))
                        region_number += 1

            if not regions:
                break

            regions.sort(key=lambda x: len(x[2]), reverse=True)
            walls_built = regions[0][0]
            walls += len(regions[0][2])

            for region_number, region, perimeter in regions:
                if region_number == walls_built:
                    for row, col in perimeter:
                        isInfected[row][col] = -1
                else:
                    spread_virus(region)

        return walls