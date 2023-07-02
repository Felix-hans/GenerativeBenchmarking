# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['_end'] = True

        def backtrack(row, col, parent):
            char = board[row][col]
            curr_node = parent[char]

            word = curr_node.pop('_end', False)
            if word:
                found_words.append(word)

            board[row][col] = '#'

            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] in curr_node:
                    backtrack(new_row, new_col, curr_node)

            board[row][col] = char

            if not curr_node:
                parent.pop(char)

        found_words = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie:
                    backtrack(row, col, trie)

        return found_words