# @lc app=leetcode id=220 lang=python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        n = len(nums)
        buckets = {}
        
        for i in range(n):
            bucket = nums[i] // (valueDiff + 1)
            
            for j in range(bucket - 1, bucket + 2):
                if j in buckets and abs(nums[i] - buckets[j]) <= valueDiff:
                    return True
            
            buckets[bucket] = nums[i]
            
            if i >= indexDiff:
                outdated_bucket = nums[i - indexDiff] // (valueDiff + 1)
                del buckets[outdated_bucket]
        
        return False