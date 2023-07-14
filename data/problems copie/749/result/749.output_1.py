# @lc app=leetcode id=749 lang=python3
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        walls = 0

        def dfs(i, j, region, perimeter):
            if i < 0 or i >= m or j < 0 or j >= n or isInfected[i][j] == 2:
                return region, perimeter
            if isInfected[i][j] == 0:
                perimeter.add((i, j))
                return region, perimeter

            isInfected[i][j] = 2
            region.add((i, j))

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                region, perimeter = dfs(ni, nj, region, perimeter)

            return region, perimeter

        def expand(region):
            growth = set()
            for i, j in region:
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and isInfected[ni][nj] == 0:
                        growth.add((ni, nj))
            return growth

        def build_walls(region):
            for i, j in region:
                isInfected[i][j] = 1
            walls_added = len(region)
            for i, j in region:
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= ni < m and 0 <= nj < n and isInfected[ni][nj] == 0:
                        isInfected[ni][nj] = 1
                        walls_added += 1
            return walls_added

        while True:
            regions = []
            perimeters = []
            visited = set()

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        region, perimeter = dfs(i, j, set(), set())
                        regions.append(region)
                        perimeters.append(perimeter)
                        visited.update(region)

            if not regions:
                break

            max_growth = set()
            max_index = -1

            for i, region in enumerate(regions):
                growth = expand(region)
                if len(growth) > len(max_growth):
                    max_growth = growth
                    max_index = i

            walls += build_walls(regions[max_index])

            for i, region in enumerate(regions):
                if i != max_index:
                    for cell in perimeters[i]:
                        isInfected[cell[0]][cell[1]] = 1

        return walls