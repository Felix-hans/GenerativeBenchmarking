# @lc app=leetcode id=2186 lang=python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict_s = {}
        dict_t = {}
        
        for c in s:
            dict_s[c] = dict_s.get(c, 0) + 1
        
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        
        steps = 0
        
        for c in s:
            if c not in t:
                steps += 1
            elif dict_s[c] > dict_t[c]:
                steps += dict_s[c] - dict_t[c]
        
        return steps