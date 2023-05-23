# @lc app=leetcode id=1 lang=python3
class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Hash map to store elements and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  # Store the element in the hash map

        return []