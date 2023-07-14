# @lc app=leetcode id=220 lang=python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        n = len(nums)
        window = {}
        
        for i in range(n):
            for j in range(max(0, i - indexDiff), i):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
            
            window[nums[i]] = window.get(nums[i], 0) + 1
            
            if i >= indexDiff:
                window[nums[i - indexDiff]] -= 1
                if window[nums[i - indexDiff]] == 0:
                    del window[nums[i - indexDiff]]
        
        return False