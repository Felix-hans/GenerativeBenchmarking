# @lc app=leetcode id=719 lang=python3
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in non-decreasing order
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0

            for i in range(n):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left