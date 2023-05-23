# @lc app=leetcode id=118 lang=python3
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        
        for i in range(numRows):
            row = [1] * (i + 1)  # Initialize each row with 1
            
            if i >= 2:
                prev_row = triangle[i - 1]
                
                for j in range(1, i):
                    row[j] = prev_row[j - 1] + prev_row[j]  # Calculate the value based on the previous row
            
            triangle.append(row)
        
        return triangle