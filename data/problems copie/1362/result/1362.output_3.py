# @lc app=leetcode id=1362 lang=python3
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        diff = float('inf')  # Initialize the minimum difference to infinity
        res = []  # Initialize the result list

        for i in range(int((num + 2) ** 0.5), 0, -1):
            if (num + 1) % i == 0:
                if abs(i - (num + 1) // i) < diff:
                    diff = abs(i - (num + 1) // i)
                    res = [i, (num + 1) // i]

            if (num + 2) % i == 0:
                if abs(i - (num + 2) // i) < diff:
                    diff = abs(i - (num + 2) // i)
                    res = [i, (num + 2) // i]

        return res