# @lc app=leetcode id=313 lang=python3
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]  # Initialize with the first super ugly number, which is 1
        ptrs = [0] * len(primes)  # Pointers for each prime factor
        
        for _ in range(n - 1):
            next_ugly_num = float('inf')  # Initialize next ugly number as positive infinity
            
            for i in range(len(primes)):
                next_num = ugly_nums[ptrs[i]] * primes[i]
                next_ugly_num = min(next_ugly_num, next_num)
            
            for i in range(len(primes)):
                if ugly_nums[ptrs[i]] * primes[i] == next_ugly_num:
                    ptrs[i] += 1
            
            ugly_nums.append(next_ugly_num)  # Add the next super ugly number to the list
        
        return ugly_nums[-1]  # Return the nth super ugly number