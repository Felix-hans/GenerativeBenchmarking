# @lc app=leetcode id=1002 lang=python3
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        char_count = {}
        for char in words[0]:
            char_count[char] = char_count.get(char, 0) + 1

        for word in words[1:]:
            temp_count = {}
            for char in word:
                if char in char_count:
                    temp_count[char] = temp_count.get(char, 0) + 1
                    if temp_count[char] > char_count[char]:
                        temp_count[char] = char_count[char]
            char_count = temp_count

        output = []
        for char, count in char_count.items():
            output.extend([char] * count)

        return output