# @lc app=leetcode id=1239 lang=python3
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, path):
            nonlocal max_length
            if len(set(path)) != len(path):
                return
            max_length = max(max_length, len(path))
            for i in range(start, len(arr)):
                backtrack(i + 1, path + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length