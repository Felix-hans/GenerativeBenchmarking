# @lc app=leetcode id=719 lang=python3
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        left, right = 0, nums[-1] - nums[0]  # Initialize the pointers

        while left < right:
            mid = (left + right) // 2
            count = 0

            for i in range(len(nums)):
                j = i + 1
                while j < len(nums) and nums[j] - nums[i] <= mid:
                    count += 1
                    j += 1

            if count >= k:
                right = mid
            else:
                left = mid + 1

        return left