# @lc app=leetcode id=1362 lang=python3
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        target1 = num + 1
        target2 = num + 2
        
        def find_divisors(target):
            for i in range(int(target**0.5), 0, -1):
                if target % i == 0:
                    return [i, target // i]
        
        divisors1 = find_divisors(target1)
        divisors2 = find_divisors(target2)
        
        return divisors1 if abs(divisors1[0] - divisors1[1]) < abs(divisors2[0] - divisors2[1]) else divisors2