# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.dp[i][j] = (
                    self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] +
                    matrix[i - 1][j - 1]
                )
    
    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.dp[row2 + 1][col2 + 1] -
            self.dp[row1][col2 + 1] -
            self.dp[row2 + 1][col1] +
            self.dp[row1][col1]
        )