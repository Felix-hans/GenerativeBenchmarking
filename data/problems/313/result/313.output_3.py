# @lc app=leetcode id=313 lang=python3
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]  # Store the super ugly numbers
        prime_factors = [0] * len(primes)  # Pointers to track the current prime factor for each prime
        
        for _ in range(1, n):
            next_ugly = float('inf')  # Initialize the next super ugly number as positive infinity
            
            for i in range(len(primes)):
                next_ugly = min(next_ugly, primes[i] * ugly_nums[prime_factors[i]])
            
            for i in range(len(primes)):
                if primes[i] * ugly_nums[prime_factors[i]] == next_ugly:
                    prime_factors[i] += 1
            
            ugly_nums.append(next_ugly)  # Add the next super ugly number to the list
        
        return ugly_nums[-1]  # Return the nth super ugly number