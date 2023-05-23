# @lc app=leetcode id=303 lang=python3
class NumArray:
    def __init__(self, nums):
        self.cumulative_sums = [0]
        cum_sum = 0
        for num in nums:
            cum_sum += num
            self.cumulative_sums.append(cum_sum)

    def sumRange(self, left, right):
        return self.cumulative_sums[right + 1] - self.cumulative_sums[left]