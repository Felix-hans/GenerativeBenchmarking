# @lc app=leetcode id=1414 lang=python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        count = 0
        index = len(fib) - 1

        while k > 0:
            if fib[index] <= k:
                k -= fib[index]
                count += 1
            index -= 1

        return count