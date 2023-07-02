# @lc app=leetcode id=719 lang=python3
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to simplify the search
        
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]  # Initialize the search space
        
        while left < right:
            mid = (left + right) // 2
            count = 0  # Count of pairs with distance <= mid
            start = 0  # Start index of the sliding window
            
            for i in range(n):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
            
            if count >= k:
                right = mid
            else:
                left = mid + 1
        
        return left