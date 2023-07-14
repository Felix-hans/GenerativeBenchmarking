# @lc app=leetcode id=566 lang=python3
class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flattened = [num for row in mat for num in row]
        
        reshaped = [flattened[i*c : (i+1)*c] for i in range(r)]
        
        return reshaped