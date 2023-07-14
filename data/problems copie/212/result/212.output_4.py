# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, word):
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == '#':
                return False
            if board[i][j] != word[0]:
                return False
            if len(word) == 1:
                return True

            char = board[i][j]
            board[i][j] = '#'

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + dx, j + dy
                if dfs(x, y, word[1:]):
                    board[i][j] = char
                    return True

            board[i][j] = char
            return False

        m, n = len(board), len(board[0])
        result = []
        
        for word in words:
            found = False
            for i in range(m):
                for j in range(n):
                    if dfs(i, j, word):
                        result.append(word)
                        found = True
                        break
                if found:
                    break

        return result