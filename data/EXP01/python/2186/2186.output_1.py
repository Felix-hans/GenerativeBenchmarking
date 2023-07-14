# @lc app=leetcode id=2186 lang=python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_s = [0] * 26
        freq_t = [0] * 26
        
        for char in s:
            freq_s[ord(char) - ord('a')] += 1
        
        for char in t:
            freq_t[ord(char) - ord('a')] += 1
        
        total_steps = 0
        for i in range(26):
            total_steps += abs(freq_s[i] - freq_t[i])
        
        return total_steps