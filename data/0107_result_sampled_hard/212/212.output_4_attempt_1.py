# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        board = [list(row) for row in board]
        
        result = set()
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def backtrack(row, col, node, parent):
            if '#' in node and node['#']:
                result.add(''.join(parent))
                node['#'] = False
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] not in node:
                return
            
            letter = board[row][col]
            board[row][col] = '#'
            
            for dx, dy in directions:
                backtrack(row + dx, col + dy, node[letter], parent + [letter])
            
            board[row][col] = letter
        
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, trie, [])
        
        return list(result)