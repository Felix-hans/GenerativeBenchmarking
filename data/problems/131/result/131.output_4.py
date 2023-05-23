# @lc app=leetcode id=131 lang=python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(s, [], result)
        return result
    
    def backtrack(self, s: str, current: List[str], result: List[List[str]]):
        if not s:
            result.append(current[:])
            return
        
        for i in range(1, len(s) + 1):
            substring = s[:i]
            if self.is_palindrome(substring):
                current.append(substring)
                self.backtrack(s[i:], current, result)
                current.pop()  # Backtrack by removing the last added palindrome substring
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]