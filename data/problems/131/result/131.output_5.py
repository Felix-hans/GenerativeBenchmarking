# @lc app=leetcode id=131 lang=python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring):
            return substring == substring[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for i in range(start, len(s)):
                substring = s[start:i+1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1, path)
                    path.pop()

        result = []
        backtrack(0, [])
        return result