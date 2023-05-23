# @lc app=leetcode id=799 lang=python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * i for i in range(1, query_row + 2)]
        glasses[0][0] = poured

        for row in range(query_row + 1):
            for glass in range(row + 1):
                if glasses[row][glass] >= 1:
                    excess = glasses[row][glass] - 1
                    glasses[row][glass] = 1
                    if row + 1 < query_row + 1:
                        glasses[row + 1][glass] += excess / 2
                        glasses[row + 1][glass + 1] += excess / 2

        return min(1, glasses[query_row][query_glass])