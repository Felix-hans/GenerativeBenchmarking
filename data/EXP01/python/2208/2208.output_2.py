# @lc app=leetcode id=2208 lang=python3
from typing import List

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        total_sum = sum(nums)
        half_sum = total_sum // 2  # Calculate half of the total sum
        current_sum = 0  # Track the sum of the reduced numbers
        
        num_operations = 0
        for num in nums:
            current_sum += num
            num_operations += 1
            if current_sum >= half_sum:
                break
        
        return num_operations