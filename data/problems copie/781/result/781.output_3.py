# @lc app=leetcode id=781 lang=python3
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {}
        rabbits = 0

        for ans in answers:
            if ans == 0:
                rabbits += 1
                continue

            if ans not in count:
                count[ans] = 1
            else:
                count[ans] += 1

            if count[ans] > ans + 1:
                count.pop(ans)
                rabbits += ans + 1

        for ans, freq in count.items():
            rabbits += ans + 1

        return rabbits