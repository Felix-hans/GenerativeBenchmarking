# @lc app=leetcode id=747 lang=python3
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)  # Find the largest element in the array
        max_index = nums.index(max_num)  # Get the index of the largest element

        for num in nums:
            if num != max_num and num * 2 > max_num:
                return -1  # The largest element is not at least twice as much as every other number

        return max_index  # Return the index of the largest element


solution = Solution()
nums = [3, 6, 1, 0]
result = solution.dominantIndex(nums)
print(result)  # Output: 1