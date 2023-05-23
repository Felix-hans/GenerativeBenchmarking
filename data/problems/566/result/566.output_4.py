# @lc app=leetcode id=566 lang=python3
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        if m * n != r * c:  # Check if reshape is possible
            return mat
        
        flattened = [element for row in mat for element in row]  # Flatten the original matrix
        
        reshaped = []
        index = 0
        
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flattened[index])
                index += 1
            reshaped.append(row)
        
        return reshaped