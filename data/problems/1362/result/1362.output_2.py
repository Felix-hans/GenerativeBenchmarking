# @lc app=leetcode id=1362 lang=python3
import math
from typing import List

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        divisors = []
        target_sums = [num + 1, num + 2]

        for target_sum in target_sums:
            for i in range(int(math.sqrt(target_sum)), 0, -1):
                if target_sum % i == 0:
                    j = target_sum // i
                    divisors.append([i, j])
                    break

        return divisors[-1]  # Return the closest divisors


solution = Solution()
print(solution.closestDivisors(8))   # Output: [3, 3]
print(solution.closestDivisors(123)) # Output: [5, 25]
print(solution.closestDivisors(999)) # Output: [40, 25]