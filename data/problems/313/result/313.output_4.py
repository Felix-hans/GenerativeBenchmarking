# @lc app=leetcode id=313 lang=python3
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglies = [1]  # List to store super ugly numbers
        pointers = [0] * len(primes)  # Pointers for each prime factor
        
        for _ in range(n - 1):  # Generate the next (n - 1) super ugly numbers
            next_ugly = min(primes[i] * uglies[pointers[i]] for i in range(len(primes)))
            uglies.append(next_ugly)
            
            for i in range(len(primes)):  # Update pointers for selected prime factors
                if primes[i] * uglies[pointers[i]] == next_ugly:
                    pointers[i] += 1
        
        return uglies[-1]  # Return the n-th super ugly number