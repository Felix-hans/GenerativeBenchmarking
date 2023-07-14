# @lc app=leetcode id=867 lang=python3
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transpose_matrix[j][i] = matrix[i][j]
        
        return transpose_matrix