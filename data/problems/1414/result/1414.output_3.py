# @lc app=leetcode id=1414 lang=python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibonacci = [1, 1]  # Fibonacci numbers: F1 = 1, F2 = 1
        while fibonacci[-1] < k:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        
        count = 0
        index = len(fibonacci) - 1
        while k > 0:
            if fibonacci[index] <= k:
                k -= fibonacci[index]
                count += 1
            index -= 1
        
        return count