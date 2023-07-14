# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(row, col, word, board):
            if not word:
                return True
            
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[0]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'
            
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if dfs(newRow, newCol, word[1:], board):
                    return True
            
            board[row][col] = temp
            return False
        
        result = []
        
        for word in words:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if dfs(row, col, word, board):
                        result.append(word)
                        break
        
        return result