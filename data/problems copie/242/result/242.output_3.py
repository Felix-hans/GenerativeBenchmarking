# @lc app=leetcode id=242 lang=python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s, key=ord) == sorted(t, key=ord)