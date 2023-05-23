# @lc app=leetcode id=628 lang=python3
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order

        max_product = nums[-1] * nums[-2] * nums[-3]

        if nums[0] < 0 and nums[1] < 0:
            max_product = max(max_product, nums[0] * nums[1] * nums[-1])

        return max_product