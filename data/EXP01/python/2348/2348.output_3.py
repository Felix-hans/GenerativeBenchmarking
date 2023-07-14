# @lc app=leetcode id=2348 lang=python3
from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        left = 0
        zeros = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            if right - left + 1 > zeros:
                count += right - left + 1 - zeros
                
            while zeros > 0:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                    
        return count