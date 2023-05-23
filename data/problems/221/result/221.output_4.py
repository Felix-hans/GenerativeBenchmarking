# @lc app=leetcode id=221 lang=python3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        max_square_size = 0
        
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    max_square_size = max(max_square_size, dp[i][j])
        
        return max_square_size * max_square_size