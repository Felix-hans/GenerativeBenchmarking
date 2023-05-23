# @lc app=leetcode id=1239 lang=python3
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, path, unique_chars):
            nonlocal max_length

            if index == len(arr) or not unique_chars:
                max_length = max(max_length, len(path))
                return

            backtrack(index + 1, path, unique_chars)

            if is_unique(arr[index], unique_chars):
                backtrack(index + 1, path + arr[index], unique_chars - set(arr[index]))

        def is_unique(s, unique_chars):
            return len(set(s)) == len(s) and set(s).isdisjoint(unique_chars)

        max_length = 0
        backtrack(0, "", set())

        return max_length