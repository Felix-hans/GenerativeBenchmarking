# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        buckets = {}  # Store the buckets and their corresponding values
        
        for i, num in enumerate(nums):
            bucket_idx = num // (valueDiff + 1)  # Calculate the bucket index
            
            for idx in range(bucket_idx - 1, bucket_idx + 2):
                if idx in buckets and abs(buckets[idx] - num) <= valueDiff:
                    return True
            
            buckets[bucket_idx] = num  # Store the current value
            
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // (valueDiff + 1)]
        
        return False