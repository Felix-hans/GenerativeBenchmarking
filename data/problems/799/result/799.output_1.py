# @lc app=leetcode id=799 lang=python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (row + 1) for row in range(query_row + 1)]
        tower[0][0] = poured  # Pour champagne into the top glass
        
        for row in range(query_row):
            for col in range(row + 1):
                excess = (tower[row][col] - 1.0) / 2
                
                if excess > 0:
                    tower[row + 1][col] += excess
                    tower[row + 1][col + 1] += excess
        
        return min(1.0, tower[query_row][query_glass])