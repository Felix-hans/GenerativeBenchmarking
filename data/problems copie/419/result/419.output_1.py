# @lc app=leetcode id=419 lang=python3
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        m, n = len(board), len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X'):
                    count += 1
        
        return count