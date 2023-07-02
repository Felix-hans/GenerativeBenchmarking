# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(i, j, word, node):
            if '#' in node and node['#']:
                result.add(word)
                node['#'] = False  # Mark word as visited
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] not in node:
                return

            letter = board[i][j]
            board[i][j] = '#'
            backtrack(i+1, j, word+letter, node[letter])
            backtrack(i-1, j, word+letter, node[letter])
            backtrack(i, j+1, word+letter, node[letter])
            backtrack(i, j-1, word+letter, node[letter])
            board[i][j] = letter

        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

        result = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                backtrack(i, j, '', trie)

        return list(result)