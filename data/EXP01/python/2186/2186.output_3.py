# @lc app=leetcode id=2186 lang=python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = {}
        
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        for char in t:
            if char in count:
                count[char] -= 1
                if count[char] == 0:
                    del count[char]
        
        min_steps = 0
        for key in count:
            min_steps += abs(count[key])
        
        return min_steps