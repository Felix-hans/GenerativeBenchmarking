# @lc app=leetcode id=1002 lang=python3
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        
        char_count = [0] * 26  # Assuming only lowercase English letters
        
        for char in words[0]:
            char_count[ord(char) - ord('a')] += 1
        
        for word in words[1:]:
            curr_count = [0] * 26
            
            for char in word:
                curr_count[ord(char) - ord('a')] += 1
            
            for i in range(26):
                char_count[i] = min(char_count[i], curr_count[i])
        
        for i in range(26):
            for _ in range(char_count[i]):
                result.append(chr(i + ord('a')))
        
        return result