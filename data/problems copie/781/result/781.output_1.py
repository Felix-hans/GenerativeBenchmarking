# @lc app=leetcode id=781 lang=python3
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        result = 0
        
        for answer in answers:
            if answer not in count:
                count[answer] = 1
            else:
                count[answer] += 1
        
        for answer, rabbits in count.items():
            result += (answer + 1) * ((rabbits + answer) // (answer + 1))
        
        return result