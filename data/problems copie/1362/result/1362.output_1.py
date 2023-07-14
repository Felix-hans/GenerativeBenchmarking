# @lc app=leetcode id=1362 lang=python3
from math import isqrt

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        num1 = num + 1
        num2 = num + 2

        for i in range(isqrt(num2), 0, -1):
            if num1 % i == 0:
                return [i, num1 // i]
            if num2 % i == 0:
                return [i, num2 // i]