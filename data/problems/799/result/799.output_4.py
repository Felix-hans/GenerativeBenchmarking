# @lc app=leetcode id=799 lang=python3
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glasses = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        glasses[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                overflow = (glasses[i][j] - 1) / 2
                if overflow > 0:
                    glasses[i + 1][j] += overflow
                    glasses[i + 1][j + 1] += overflow

        return min(1, glasses[query_row][query_glass])