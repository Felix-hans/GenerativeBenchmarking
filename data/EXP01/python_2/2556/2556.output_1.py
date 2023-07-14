# @lc app=leetcode id=2556 lang=python
class Solution:
        def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
            m, n = len(grid), len(grid[0])
            if grid[0][0] == 0 or grid[m-1][n-1] == 0:
                return False

            def dfs(i, j):
                if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                    return False
                if i == m-1 and j == n-1:
                    return True
                grid[i][j] = 0
                return dfs(i+1, j) or dfs(i, j+1)

            if dfs(0, 0):
                return True

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                        if dfs(0, 0):
                            return True
                        grid[i][j] = 0

            return False