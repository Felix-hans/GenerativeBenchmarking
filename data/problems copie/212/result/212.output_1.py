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
            node['$'] = True
        
        def dfs(row, col, node, path):
            if '$' in node:
                result.append(path)
                del node['$']  # Remove word from trie to avoid duplicates
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] not in node:
                return
            
            char = board[row][col]
            
            board[row][col] = '#'
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                dfs(new_row, new_col, node[char], path + char)
            
            board[row][col] = char
        
        result = []
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie:
                    dfs(row, col, trie, "")
        
        return result