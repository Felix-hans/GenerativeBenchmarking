# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix_sums = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.prefix_sums = [[0] * (n + 1) for _ in range(m)]
            
            for i in range(m):
                for j in range(n):
                    self.prefix_sums[i][j + 1] = self.prefix_sums[i][j] + matrix[i][j]
                    
            for i in range(1, m):
                for j in range(n + 1):
                    self.prefix_sums[i][j] += self.prefix_sums[i - 1][j]
    
    def sumRegion(self, row1, col1, row2, col2):
        if self.prefix_sums is None:
            return 0
        
        upper_left = self.prefix_sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        upper_right = self.prefix_sums[row1 - 1][col2] if row1 > 0 else 0
        lower_left = self.prefix_sums[row2][col1 - 1] if col1 > 0 else 0
        lower_right = self.prefix_sums[row2][col2]
        
        return lower_right - upper_right - lower_left + upper_left