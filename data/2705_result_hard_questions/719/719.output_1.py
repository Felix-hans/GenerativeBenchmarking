# @lc app=leetcode id=719 lang=python3
from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        
        left = 0
        right = nums[n-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            count = 0  # Count of pairs with distance <= mid
            j = 0  # Pointer for the second element in the pair
            
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1
            
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left