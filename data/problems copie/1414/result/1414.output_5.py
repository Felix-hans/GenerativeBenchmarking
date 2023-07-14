# @lc app=leetcode id=1414 lang=python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_nums = [1, 1]  # Initialize the list of Fibonacci numbers with F1 = 1 and F2 = 1
        while fib_nums[-1] < k:
            next_fib = fib_nums[-1] + fib_nums[-2]
            fib_nums.append(next_fib)

        count = 0
        i = len(fib_nums) - 1  # Start from the largest Fibonacci number
        while k > 0:
            if fib_nums[i] <= k:
                k -= fib_nums[i]
                count += 1
            else:
                i -= 1  # Move to the next smaller Fibonacci number

        return count