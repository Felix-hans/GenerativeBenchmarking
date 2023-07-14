# @lc app=leetcode id=217 lang=python3
class Solution:
    def containsDuplicate(self, nums):
        unique_nums = set()
        
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.add(num)
        
        return False