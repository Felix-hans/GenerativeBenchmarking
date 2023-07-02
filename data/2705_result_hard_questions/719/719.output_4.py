# @lc app=leetcode id=719 lang=python3
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        left = 0  # Smallest possible distance
        right = nums[-1] - nums[0]  # Largest possible distance
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            start = 0
            
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            
            if count >= k:
                right = mid
            else:
                left = mid + 1
        
        return left