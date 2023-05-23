# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_set = set(words)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, word, visited):
            if word in words_set:
                result.append(word)
                words_set.remove(word)  # Remove the word to avoid duplicates

            visited[row][col] = True

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if (
                    0 <= new_row < len(board) and
                    0 <= new_col < len(board[0]) and
                    not visited[new_row][new_col] and
                    board[new_row][new_col] in word
                ):
                    dfs(new_row, new_col, word + board[new_row][new_col], visited)

            visited[row][col] = False

        result = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, board[i][j], visited)

        return result