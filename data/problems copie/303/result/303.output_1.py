# @lc app=leetcode id=303 lang=python3
class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = self.calculate_prefix_sum()

    def calculate_prefix_sum(self):
        prefix_sum = [0]
        current_sum = 0
        for num in self.nums:
            current_sum += num
            prefix_sum.append(current_sum)
        return prefix_sum

    def sumRange(self, left, right):
        return self.prefix_sum[right + 1] - self.prefix_sum[left]