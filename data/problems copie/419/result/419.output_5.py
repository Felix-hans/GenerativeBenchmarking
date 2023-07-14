# @lc app=leetcode id=419 lang=python3
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows, cols = len(board), len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                count += 1
                
        return count