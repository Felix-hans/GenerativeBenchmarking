# @lc app=leetcode id=118 lang=python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        if numRows == 0:
            return triangle
        
        triangle.append([1])
        
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            curr_row = [1]
            
            for j in range(1, i):
                curr_row.append(prev_row[j - 1] + prev_row[j])
            
            curr_row.append(1)
            
            triangle.append(curr_row)
        
        return triangle