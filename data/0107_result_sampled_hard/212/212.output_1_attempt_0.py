# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True  # '#' denotes the end of a word
        
        def backtrack(row, col, parent):
            letter = board[row][col]
            curr_node = parent[letter]
            
            word = curr_node.pop('#', False)
            if word:
                found_words.append(word)
            
            board[row][col] = '#'  # Mark the cell as visited
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] in curr_node:
                    backtrack(new_row, new_col, curr_node)
            
            board[row][col] = letter  # Mark the cell as unvisited
            
            if not curr_node:
                parent.pop(letter)
        
        found_words = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        
        return found_words