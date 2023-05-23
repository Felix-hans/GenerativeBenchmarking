# @lc app=leetcode id=688 lang=python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        
        dp[0][row][column] = 1
        
        for m in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for move in moves:
                        prev_r, prev_c = r - move[0], c - move[1]
                        if 0 <= prev_r < n and 0 <= prev_c < n:
                            dp[m][r][c] += dp[m-1][prev_r][prev_c] / 8.0
        
        probability = sum(sum(row) for row in dp[k])
        return probability