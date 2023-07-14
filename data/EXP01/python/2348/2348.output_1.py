# @lc app=leetcode id=2348 lang=python3
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        subarray_zeros = 0
        for num in nums:
            if num == 0:
                subarray_zeros += 1
                count += subarray_zeros
            else:
                subarray_zeros = 0
        return count