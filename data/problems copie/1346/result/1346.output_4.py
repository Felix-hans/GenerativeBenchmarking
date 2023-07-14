# @lc app=leetcode id=1346 lang=python3
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()  # to store the visited elements
        for num in arr:
            if 2 * num in seen or num % 2 == 0 and num // 2 in seen:
                return True
            seen.add(num)
        return False