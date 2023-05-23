# @lc app=leetcode id=961 lang=python3
class Solution:
    def repeatedNTimes(self, nums):
        count = {}
        for num in nums:
            if num in count:
                return num
            count[num] = 1