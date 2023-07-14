# @lc app=leetcode id=2491 lang=python3
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n % 2 != 0:
            return -1
        
        skill_counts = {}
        for s in skill:
            skill_counts[s] = skill_counts.get(s, 0) + 1
        
        for s, count in skill_counts.items():
            if count % 2 != 0:
                return -1
        
        chemistry_sum = 0
        for s, count in skill_counts.items():
            chemistry = s * (count // 2) * (count // 2)
            chemistry_sum += chemistry
        
        return chemistry_sum