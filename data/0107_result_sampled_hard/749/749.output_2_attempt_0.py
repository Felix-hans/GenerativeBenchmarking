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

        def get_region(row, col, region_number):
            region = set([(row, col)])
            queue = [(row, col)]
            while queue:
                r, c = queue.pop(0)
                for nr, nc in get_neighbors(r, c):
                    if isInfected[nr][nc] == 1 and (nr, nc) not in region:
                        region.add((nr, nc))
                        queue.append((nr, nc))
                        isInfected[nr][nc] = region_number

        def build_walls(region_number):
            region = set()
            perimeter = set()
            for row in range(m):
                for col in range(n):
                    if isInfected[row][col] == region_number:
                        region.add((row, col))
                        for nr, nc in get_neighbors(row, col):
                            if isInfected[nr][nc] == 0:
                                perimeter.add((nr, nc))
            for row, col in perimeter:
                isInfected[row][col] = -1

            return len(perimeter)

        def spread_virus(region_number):
            queue = []
            for row in range(m):
                for col in range(n):
                    if isInfected[row][col] == region_number:
                        for nr, nc in get_neighbors(row, col):
                            if isInfected[nr][nc] == 0:
                                isInfected[nr][nc] = 1
                                queue.append((nr, nc))
            return queue

        while True:
            regions = []
            region_number = 2
            walls_built = 0

            for row in range(m):
                for col in range(n):
                    if isInfected[row][col] == 1:
                        get_region(row, col, region_number)
                        regions.append(region_number)
                        region_number += 1

            if not regions:
                break

            regions_count = len(regions)
            max_perimeter = 0
            for region in regions:
                perimeter = build_walls(region)
                if perimeter > max_perimeter:
                    max_perimeter = perimeter
                    walls_built = region

            walls += build_walls(walls_built)

            for region in regions:
                if region != walls_built:
                    spread_virus(region)

        return walls