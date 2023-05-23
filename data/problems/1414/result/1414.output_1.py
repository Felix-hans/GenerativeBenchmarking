# @lc app=leetcode id=1414 lang=python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib_nums = [1, 1]
        while fib_nums[-1] < k:
            fib_nums.append(fib_nums[-1] + fib_nums[-2])
        
        count = 0
        for i in range(len(fib_nums) - 1, -1, -1):
            if k >= fib_nums[i]:
                count += 1
                k -= fib_nums[i]
            if k == 0:
                break
        
        return count