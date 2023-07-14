# @lc app=leetcode id=561 lang=python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        pair_sum = 0
        for i in range(0, len(nums), 2):
            pair_sum += nums[i]  # Add the minimum element from each pair
        return pair_sum