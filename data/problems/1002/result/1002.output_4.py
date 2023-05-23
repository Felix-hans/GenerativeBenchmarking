# @lc app=leetcode id=1002 lang=python3
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
        
        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1
        
        for word in words[1:]:
            word_count = {}
            
            for char in word:
                word_count[char] = word_count.get(char, 0) + 1
            
            common_chars = []
            for char in char_count:
                if char in word_count:
                    common_chars.extend([char] * min(char_count[char], word_count[char]))
            
            char_count = word_count
        
        return common_chars