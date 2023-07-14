# @lc app=leetcode id=2556 lang=python
class Solution:
    def isPossibleToCutPath(self, grid):
        m, n = len(grid), len(grid[0])
        
        def bfs():
            queue = [(0, 0)]
            visited = set()
            
            while queue:
                row, col = queue.pop(0)
                
                if row == m-1 and col == n-1:
                    return True
                
                visited.add((row, col))
                
                for dx, dy in [(1, 0), (0, 1)]:
                    new_row, new_col = row + dx, col + dy
                    
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
            
            return False
        
        if bfs():
            return True
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    
                    if not bfs():
                        return True
                    
                    grid[row][col] = 1
                    
        return False