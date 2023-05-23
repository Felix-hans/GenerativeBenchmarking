# @lc app=leetcode id=303 lang=python3
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = self.calculate_prefix_sum()

    def calculate_prefix_sum(self):
        prefix_sum = [0] * (len(self.nums) + 1)
        for i in range(1, len(self.nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + self.nums[i - 1]
        return prefix_sum

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]