# @lc app=leetcode id=1 lang=python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices = {}  # dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in num_indices:
                return [num_indices[complement], i]
            
            num_indices[num] = i
        
        return []