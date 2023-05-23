# @lc app=leetcode id=324 lang=python3
class Solution:
    def wiggleSort(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        mid = len(nums) // 2
        left = mid - 1 if len(nums) % 2 == 0 else mid
        right = len(nums) - 1

        result = [0] * len(nums)

        for i in range(len(result)):
            if i % 2 == 0:
                result[i] = nums[left]
                left -= 1
            else:
                result[i] = nums[right]
                right -= 1

        for i in range(len(nums)):
            nums[i] = result[i]