# @lc app=leetcode id=749 lang=python3
class Solution:
    def containVirus(self, isInfected):
        def spread_virus(grid, row, col, visited):
            if (
                row < 0
                or row >= len(grid)
                or col < 0
                or col >= len(grid[0])
                or grid[row][col] == 2
                or (row, col) in visited
            ):
                return 0
            
            if grid[row][col] == 0:
                grid[row][col] = 1
                visited.add((row, col))
                return 1 + (
                    spread_virus(grid, row + 1, col, visited)
                    + spread_virus(grid, row - 1, col, visited)
                    + spread_virus(grid, row, col + 1, visited)
                    + spread_virus(grid, row, col - 1, visited)
                )
            
            return 0
        
        walls = 0
        days = 0
        
        while True:
            max_region = set()
            max_walls = 0
            max_neighbors = 0
            
            for i in range(len(isInfected)):
                for j in range(len(isInfected[0])):
                    if isInfected[i][j] == 1:
                        visited = set()
                        newly_infected = spread_virus(isInfected, i, j, visited)
                        
                        region = set(visited)
                        neighbors = set()
                        
                        for row, col in visited:
                            if (
                                row > 0 and isInfected[row - 1][col] == 0
                                or row < len(isInfected) - 1 and isInfected[row + 1][col] == 0
                                or col > 0 and isInfected[row][col - 1] == 0
                                or col < len(isInfected[0]) - 1 and isInfected[row][col + 1] == 0
                            ):
                                if row > 0 and isInfected[row - 1][col] == 0:
                                    neighbors.add((row - 1, col))
                                if row < len(isInfected) - 1 and isInfected[row + 1][col] == 0:
                                    neighbors.add((row + 1, col))
                                if col > 0 and isInfected[row][col - 1] == 0:
                                    neighbors.add((row, col - 1))
                                if col < len(isInfected[0]) - 1 and isInfected[row][col + 1] == 0:
                                    neighbors.add((row, col + 1))
                        
                        if len(neighbors) > max_neighbors:
                            max_region = region
                            max_walls = len(neighbors)
                            max_neighbors = len(neighbors)
                        elif len(neighbors) == max_neighbors and len(neighbors) > 0:
                            if len(neighbors) > max_walls:
                                max_region = region
                                max_walls = len(neighbors)
                                max_neighbors = len(neighbors)
            
            if not max_region:
                break
            
            walls += max_walls
            
            for row, col in max_region:
                isInfected[row][col] = 2
            
            days += 1
        
        return walls