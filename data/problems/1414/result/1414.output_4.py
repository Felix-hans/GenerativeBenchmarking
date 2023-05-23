# @lc app=leetcode id=1414 lang=python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_nums = [1, 1]
        while fib_nums[-1] < k:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        
        count = 0
        index = len(fib_nums) - 1
        while k > 0:
            if fib_nums[index] <= k:
                count += 1
                k -= fib_nums[index]
            index -= 1
        
        return count