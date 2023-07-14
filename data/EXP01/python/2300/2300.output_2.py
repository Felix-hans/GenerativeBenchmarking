# @lc app=leetcode id=2300 lang=python3
class Solution:
    def successfulPairs(self, spells, potions, success):
        max_spell = max(spells)
        counter = [0] * (max_spell + 1)
        
        for potion in potions:
            for spell in spells:
                if potion * spell >= success:
                    counter[spell] += 1
                    break
        
        return counter