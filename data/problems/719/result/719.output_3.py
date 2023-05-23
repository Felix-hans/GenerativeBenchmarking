# @lc app=leetcode id=719 lang=python3
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()  # Step 1
        left, right = 0, nums[-1] - nums[0]  # Step 2

        while left < right:  # Step 3
            mid = (left + right) // 2
            count = 0

            i = 0
            for j in range(len(nums)):
                while nums[j] - nums[i] > mid:
                    i += 1
                count += j - i

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left  # Step 4