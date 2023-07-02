# @lc app=leetcode id=719 lang=python3
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()  # Sort the array in ascending order
        left, right = 0, nums[-1] - nums[0]  # Initialize the search space
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0
            
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left