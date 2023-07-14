# @lc app=leetcode id=1567 lang=python3
from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        negative_count = 0
        first_negative_index = -1
        zero_index = -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                negative_count += 1
                if first_negative_index == -1:
                    first_negative_index = i
            elif nums[i] == 0:
                negative_count = 0
                first_negative_index = -1
                zero_index = i
            if negative_count % 2 == 0:
                max_len = max(max_len, i - zero_index)
            else:
                max_len = max(max_len, i - first_negative_index)
        
        return max_len