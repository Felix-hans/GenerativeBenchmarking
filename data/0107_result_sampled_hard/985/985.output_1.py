# @lc app=leetcode id=985 lang=python3
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = sum(num for num in nums if num % 2 == 0)
        
        for query in queries:
            val, index = query
            prev_num = nums[index]
            
            nums[index] += val
            
            is_prev_even = prev_num % 2 == 0
            is_updated_even = nums[index] % 2 == 0
            
            if is_prev_even:
                even_sum -= prev_num
            if is_updated_even:
                even_sum += nums[index]
            
            result.append(even_sum)
        
        return result