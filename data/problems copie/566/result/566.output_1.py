# @lc app=leetcode id=566 lang=python3
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flattened = [num for row in mat for num in row]
        
        reshaped = [flattened[i:i+c] for i in range(0, len(flattened), c)]
        
        return reshaped