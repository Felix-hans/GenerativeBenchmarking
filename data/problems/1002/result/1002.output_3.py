# @lc app=leetcode id=1002 lang=python3
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []

        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        for word in words[1:]:
            curr_count = {}
            for char in word:
                curr_count[char] = curr_count.get(char, 0) + 1

            for char in char_count.keys():
                if char in curr_count:
                    char_count[char] = min(char_count[char], curr_count[char])
                else:
                    char_count[char] = 0

        for char, count in char_count.items():
            common_chars.extend([char] * count)

        return common_chars