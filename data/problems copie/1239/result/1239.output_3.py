# @lc app=leetcode id=1239 lang=python3
from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(arr, index, curr):
            if len(set(curr)) != len(curr):
                return 0
            
            max_length = len(curr)
            
            for i in range(index, len(arr)):
                max_length = max(max_length, backtrack(arr, i + 1, curr + arr[i]))
            
            return max_length
        
        return backtrack(arr, 0, "")