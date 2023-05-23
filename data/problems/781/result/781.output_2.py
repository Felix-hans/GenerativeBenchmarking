# @lc app=leetcode id=781 lang=python3
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        total = 0

        for ans in answers:
            if ans == 0:
                total += 1
            elif ans not in count or count[ans] == 0:
                count[ans] = ans
                total += ans + 1
            else:
                count[ans] -= 1

        return total