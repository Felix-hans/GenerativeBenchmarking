# @lc app=leetcode id=985 lang=python3
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)  # Compute the initial sum of even values
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]  # Subtract the previous even value from the sum
            
            nums[index] += val  # Update the element at the given index
            if nums[index] % 2 == 0:
                even_sum += nums[index]  # Add the new even value to the sum
            
            result.append(even_sum)  # Append the current sum of even values to the result
        
        return result