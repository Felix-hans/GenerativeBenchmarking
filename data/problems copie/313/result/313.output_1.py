# @lc app=leetcode id=313 lang=python3
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        pointers = [0] * len(primes)
        
        for i in range(1, n):
            min_val = float('inf')
            for j in range(len(primes)):
                min_val = min(min_val, ugly[pointers[j]] * primes[j])
            
            ugly[i] = min_val
            
            for j in range(len(primes)):
                if ugly[i] == ugly[pointers[j]] * primes[j]:
                    pointers[j] += 1
        
        return ugly[-1]