# @lc app=leetcode id=324 lang=python3
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        n = len(nums)
        mid = (n - 1) // 2

        subarray1 = nums[mid+1:]
        subarray2 = nums[:mid+1]

        nums[::2] = subarray1[::-1]
        nums[1::2] = subarray2[::-1]