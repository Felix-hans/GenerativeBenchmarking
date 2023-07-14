# @lc app=leetcode id=313 lang=python3
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]  # List to store super ugly numbers
        ptrs = [0] * len(primes)  # Pointers for each prime factor
        
        for _ in range(n-1):
            next_nums = [ugly_nums[ptrs[i]] * primes[i] for i in range(len(primes))]
            min_num = min(next_nums)
            ugly_nums.append(min_num)
            
            for i in range(len(primes)):
                if next_nums[i] == min_num:
                    ptrs[i] += 1
        
        return ugly_nums[-1]