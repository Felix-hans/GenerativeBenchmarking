# @lc app=leetcode id=719 lang=python3
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the input array in non-decreasing order
        left, right = 0, nums[-1] - nums[0]  # Set the search space boundaries
        
        while left < right:
            mid = (left + right) // 2  # Calculate the mid value of the search space
            count = 0  # Count of pairs with distance <= mid
            start = 0  # Start index of the sliding window
            
            for end in range(len(nums)):
                while nums[end] - nums[start] > mid:
                    start += 1
                count += end - start
            
            if count >= k:
                right = mid
            else:
                left = mid + 1
        
        return left