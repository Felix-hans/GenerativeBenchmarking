# @lc app=leetcode id=1358 lang=python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        char_count = {'a': 0, 'b': 0, 'c': 0}
        left, right, count = 0, 0, 0
        result = 0
        
        while right < n:
            char_count[s[right]] += 1
            
            while all(char_count.values()):
                char_count[s[left]] -= 1
                left += 1
            
            count += left
            
            right += 1
            result += count
        
        return result