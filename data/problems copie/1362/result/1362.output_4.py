# @lc app=leetcode id=1362 lang=python3
from math import isqrt

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for i in range(isqrt(num + 2), 0, -1):
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]