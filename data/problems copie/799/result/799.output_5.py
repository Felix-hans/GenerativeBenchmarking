# @lc app=leetcode id=799 lang=python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * i for i in range(1, query_row + 2)]
        glasses[0][0] = poured  # Pour the initial amount of champagne into the top glass
        
        for row in range(query_row + 1):
            for col in range(row + 1):
                excess = max(0, glasses[row][col] - 1)
                
                if row + 1 < len(glasses):
                    glasses[row + 1][col] += excess / 2
                    glasses[row + 1][col + 1] += excess / 2
                
                glasses[row][col] = min(1, glasses[row][col])
        
        return glasses[query_row][query_glass]