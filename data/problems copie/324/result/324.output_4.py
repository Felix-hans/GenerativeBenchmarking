# @lc app=leetcode id=324 lang=python3
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()  # Step 1
        n = len(nums)
        result = [0] * n
        left = n // 2 - 1 if n % 2 == 0 else n // 2
        right = n - 1

        for i in range(n-1, -1, -1):  # Step 4
            if i % 2 == 0:
                result[left] = nums[i]
                left -= 1
            else:
                result[right] = nums[i]
                right -= 1

        nums[:] = result  # Step 5