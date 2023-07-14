# @lc app=leetcode id=2369 lang=python3
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            if i + 1 < n and nums[i] == nums[i + 1]:
                return True

            if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]:
                return True

            if i + 2 < n and nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                return True

        return False