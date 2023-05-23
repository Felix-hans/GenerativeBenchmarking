# @lc app=leetcode id=1239 lang=python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(arr, index, current):
            nonlocal max_length
            if len(set(current)) == len(current):
                max_length = max(max_length, len(current))

            for i in range(index, len(arr)):
                new_str = current + arr[i]
                if len(set(new_str)) == len(new_str):
                    backtrack(arr, i + 1, new_str)

        max_length = 0
        backtrack(arr, 0, "")
        return max_length