# @lc app=leetcode id=893 lang=python3
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_special_equiv_representation(word):
            even_chars = sorted(word[0::2])
            odd_chars = sorted(word[1::2])
            return ''.join(even_chars) + ''.join(odd_chars)
        
        groups = set()
        for word in words:
            representation = get_special_equiv_representation(word)
            groups.add(representation)
        
        return len(groups)