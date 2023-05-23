# @lc app=leetcode id=688 lang=python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        
        dp[0][row][column] = 1
        
        for step in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp[step][r][c] += dp[step-1][nr][nc] / 8
        
        prob = sum(sum(row) for row in dp[k])
        
        return prob