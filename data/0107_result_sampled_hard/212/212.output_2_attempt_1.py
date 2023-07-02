# @lc app=leetcode id=212 lang=python3
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        grid = [list(row) for row in board]
        
        found_words = set(words)
        
        result = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.dfs(grid, i, j, "", found_words, result)
        
        return result
    
    def dfs(self, grid: List[List[str]], i: int, j: int, curr_word: str, found_words: set, result: List[str]):
        if (
            i < 0 or i >= len(grid) or
            j < 0 or j >= len(grid[0]) or
            grid[i][j] == "#"
        ):
            return
        
        curr_word += grid[i][j]
        
        if not any(word.startswith(curr_word) for word in found_words):
            return
        
        if curr_word in found_words:
            found_words.remove(curr_word)
            result.append(curr_word)
        
        temp = grid[i][j]
        grid[i][j] = "#"
        
        self.dfs(grid, i + 1, j, curr_word, found_words, result)
        self.dfs(grid, i - 1, j, curr_word, found_words, result)
        self.dfs(grid, i, j + 1, curr_word, found_words, result)
        self.dfs(grid, i, j - 1, curr_word, found_words, result)
        
        grid[i][j] = temp