# @lc app=leetcode id=2348 lang=python
class Solution:
    def zeroFilledSubarray(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                j = i - 1
                while j >= 0 and nums[j] == 0:
                    count += 1
                    j -= 1
        return count