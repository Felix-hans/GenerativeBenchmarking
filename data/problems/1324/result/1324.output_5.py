# @lc app=leetcode id=1324 lang=python3
from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_length = max(len(word) for word in words)
        result = []

        for i in range(max_length):
            temp_str = ''
            for word in words:
                if i < len(word):
                    temp_str += word[i]
                else:
                    temp_str += ' '
            result.append(temp_str.rstrip())

        return result