# @lc app=leetcode id=867 lang=python3
class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        transposed = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        
        return transposed