# @lc app=leetcode id=688 lang=python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
        dp[row][column][0] = 1
        
        for m in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for move in moves:
                        new_i, new_j = i + move[0], j + move[1]
                        if 0 <= new_i < n and 0 <= new_j < n:
                            dp[i][j][m] += dp[new_i][new_j][m - 1] / 8
        
        return sum(sum(row) for row in dp[row][column])  # Probability of staying on board