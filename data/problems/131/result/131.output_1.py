# @lc app=leetcode id=131 lang=python3
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, [], result)
        return result

    def backtrack(self, s, path, result):
        if not s:
            result.append(path[:])
            return
        
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                path.append(prefix)
                self.backtrack(s[i:], path, result)
                path.pop()

    def is_palindrome(self, s):
        return s == s[::-1]