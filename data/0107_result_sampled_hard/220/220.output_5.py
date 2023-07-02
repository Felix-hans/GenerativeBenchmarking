# @lc app=leetcode id=220 lang=python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        n = len(nums)
        buckets = {}  # Dictionary to store the buckets

        for i in range(n):
            bucket = nums[i] // (valueDiff + 1)
            offset = 1

            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = nums[i]

            if i >= indexDiff:
                prev_bucket = nums[i - indexDiff] // (valueDiff + 1)
                if prev_bucket in buckets and nums[i - indexDiff] == buckets[prev_bucket]:
                    del buckets[prev_bucket]

        return False