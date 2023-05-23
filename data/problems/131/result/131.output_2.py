# @lc app=leetcode id=131 lang=python3
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, [], result)
        return result

    def backtrack(self, s: str, current: List[str], result: List[List[str]]):
        if not s:
            result.append(current[:])  # Add a copy of the current partition to the result
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                current.append(prefix)
                self.backtrack(s[i:], current, result)
                current.pop()  # Backtrack by removing the last palindrome added

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]