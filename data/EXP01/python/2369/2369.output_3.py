# @lc app=leetcode id=2369 lang=python3
from typing import List

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n < 3:  # If the array has less than 3 elements, it is not possible to have a valid partition
            return False
        
        start, end = 0, 1  # Initialize the start and end indices of the current partition
        
        for i in range(2, n):
            if nums[i] == nums[i-1] == nums[i-2]:
                continue  # Case 1: Subarray with exactly 3 equal elements
            elif nums[i] == nums[i-1]:
                if start == end:  # Case 2: Subarray with exactly 2 equal elements
                    end = i
                else:
                    start = i-1  # Start a new partition
                    end = i
            elif nums[i] == nums[i-1] + 1 == nums[i-2] + 2:
                continue  # Case 3: Subarray with exactly 3 consecutive increasing elements
            else:
                start = i  # Start a new partition
        
        return start < end  # Check if the last partition is valid