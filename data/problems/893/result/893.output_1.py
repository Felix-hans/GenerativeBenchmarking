# @lc app=leetcode id=893 lang=python3
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:
            even_chars = sorted(word[::2])
            odd_chars = sorted(word[1::2])
            normalized_word = ''.join(even_chars) + ''.join(odd_chars)
            groups.add(normalized_word)
        
        return len(groups)