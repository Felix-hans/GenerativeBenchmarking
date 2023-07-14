# @lc app=leetcode id=2491 lang=python3
class Solution:
    def dividePlayers(self, skill):
        n = len(skill)
        total_sum = sum(skill)
        if total_sum % (n // 2) != 0:
            return -1
        
        team_sum = total_sum // (n // 2)
        skill.sort(reverse=True)
        
        chemistries = []
        i, j = 0, n-1
        while i < j:
            if skill[i] + skill[j] != team_sum:
                return -1
            chemistries.append(skill[i] * skill[j])
            i += 1
            j -= 1
        
        return sum(chemistries)