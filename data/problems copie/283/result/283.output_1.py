# @lc app=leetcode id=283 lang=python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_index] = nums[zero_index], nums[i]
                zero_index += 1

        for i in range(zero_index, len(nums)):
            nums[i] = 0