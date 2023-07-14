# @lc app=leetcode id=2420 lang=python3
from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(k, n-k):
            left_subarray = nums[i-k:i]  # Elements just before the index i
            right_subarray = nums[i+1:i+k+1]  # Elements just after the index i
            
            if left_subarray == sorted(left_subarray, reverse=True) and right_subarray == sorted(right_subarray):
                result.append(i)
        
        return result