# @lc app=leetcode id=2348 lang=python3
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:    
        subarray_count = 0
        zeros_length = 0
        
        for num in nums:
            if num != 0:
                zeros_length = 0
            else:
                zeros_length += 1
                subarray_count += zeros_length * (zeros_length + 1) // 2
        
        return subarray_count