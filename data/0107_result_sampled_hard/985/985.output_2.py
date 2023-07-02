# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        result = []
        even_sum = sum(x for x in nums if x % 2 == 0)

        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            result.append(even_sum)

        return result