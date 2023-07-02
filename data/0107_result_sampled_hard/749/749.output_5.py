# @lc app=leetcode id=749 lang=python3
from typing import List

class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        while True:
            regions = self.get_infected_regions(isInfected)
            if not regions:
                break

            walls_to_build = []
            max_threatened = 0
            max_region_index = -1

            for i, region in enumerate(regions):
                threatened = self.count_threatened_cells(region, isInfected)
                if threatened > max_threatened:
                    max_threatened = threatened
                    max_region_index = i
                    walls_to_build = self.get_walls_to_build(region, isInfected)

            walls += len(walls_to_build)
            isInfected = self.build_walls(walls_to_build, isInfected)
            self.spread_virus(isInfected)

        return walls

    def get_infected_regions(self, isInfected: List[List[int]]) -> List[List[List[int]]]:
        m, n = len(isInfected), len(isInfected[0])
        visited = [[False] * n for _ in range(m)]
        regions = []

        for i in range(m):
            for j in range(n):
                if isInfected[i][j] == 1 and not visited[i][j]:
                    region = []
                    self.dfs(i, j, isInfected, visited, region)
                    regions.append(region)

        return regions if regions else []  # Return an empty list if no regions are found

    def dfs(self, row: int, col: int, isInfected: List[List[int]], visited: List[List[bool]], region: List[List[int]]):
        m, n = len(isInfected), len(isInfected[0])

        if row < 0 or row >= m or col < 0 or col >= n or visited[row][col] or isInfected[row][col] == 0:
            return

        visited[row][col] = True
        region.append([row, col])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            self.dfs(nx, ny, isInfected, visited, region)

    def count_threatened_cells(self, region: List[List[int]], isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        count = 0

        for row, col in region:
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                if nx >= 0 and nx < m and ny >= 0 and ny < n and isInfected[nx][ny] == 0:
                    count += 1

        return count

    def get_walls_to_build(self, region: List[List[int]], isInfected: List[List[int]]) -> List[List[int]]:
        walls = []
        m, n = len(isInfected), len(isInfected[0])

        for row, col in region:
            directions = [(0, 1), (0, -1), (1, 0