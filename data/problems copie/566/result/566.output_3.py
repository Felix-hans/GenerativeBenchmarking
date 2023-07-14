# @lc app=leetcode id=566 lang=python3
class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)  # Number of rows in the original matrix
        n = len(mat[0])  # Number of columns in the original matrix
        
        if m * n != r * c:
            return mat
        
        flattened = [element for row in mat for element in row]
        
        reshaped = [flattened[i*c:(i+1)*c] for i in range(r)]
        
        return reshaped