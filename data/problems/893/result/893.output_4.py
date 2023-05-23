# @lc app=leetcode id=893 lang=python3
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        signature_set = set()

        for word in words:
            even_chars = sorted(word[0::2])  # Sort characters at even indices
            odd_chars = sorted(word[1::2])  # Sort characters at odd indices
            signature = ''.join(even_chars) + ''.join(odd_chars)
            signature_set.add(signature)

        return len(signature_set)