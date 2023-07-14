# @lc app=leetcode id=118 lang=python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle