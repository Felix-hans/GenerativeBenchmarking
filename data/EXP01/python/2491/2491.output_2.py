# @lc app=leetcode id=2491 lang=python3
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        
        freq = {}
        for s in skill:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        
        result = 0
        for s, f in freq.items():
            if s in freq and freq[s] >= 2:
                team_skill = s * f * 2
                result += team_skill
                freq[s] -= 2
        
        if sum(freq.values()) == 0:
            return result
        else:
            return -1