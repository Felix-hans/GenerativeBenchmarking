# @lc app=leetcode id=2420 lang=python3
from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        good_indices = []
        
        for i in range(k, n - k):
            if (
                nums[i-k:i] == sorted(nums[i-k:i], reverse=True) and
                nums[i+1:i+k+1] == sorted(nums[i+1:i+k+1])
            ):
                good_indices.append(i)
        
        return good_indices