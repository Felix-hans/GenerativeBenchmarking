# @lc app=leetcode id=799 lang=python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0.0] * (row + 1) for row in range(query_row + 1)]

        tower[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                excess = max(0.0, tower[i][j] - 1)

                tower[i + 1][j] += excess / 2
                tower[i + 1][j + 1] += excess / 2

        return min(1.0, tower[query_row][query_glass])