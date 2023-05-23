# @lc app=leetcode id=1 lang=python3
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}  # Hash table to store complement of each number
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]  # Return the indices if complement exists in the hash table
            num_dict[num] = i  # Store the number and its index in the hash table
        
        return []  # Return empty list if no solution is found