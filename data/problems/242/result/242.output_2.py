# @lc app=leetcode id=242 lang=python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency = {}
        
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        
        for char in t:
            frequency[char] = frequency.get(char, 0) - 1
            if frequency[char] < 0:
                return False
        
        return True