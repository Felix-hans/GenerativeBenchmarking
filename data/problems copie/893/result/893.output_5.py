# @lc app=leetcode id=893 lang=python3
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()
        for word in words:
            even_chars = ''.join(sorted(word[::2]))
            odd_chars = ''.join(sorted(word[1::2]))
            groups.add((even_chars, odd_chars))
        return len(groups)