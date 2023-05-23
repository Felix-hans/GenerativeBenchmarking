# @lc app=leetcode id=893 lang=python3
from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            even = ''.join(sorted(word[::2]))
            odd = ''.join(sorted(word[1::2]))
            groups.add((even, odd))

        return len(groups)