# @lc app=leetcode id=561 lang=python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]  # Add the minimum value of each pair to the result
        return result