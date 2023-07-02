# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = {}  # Dictionary to store elements within the sliding window
        for i, num in enumerate(nums):
            for j in range(max(num - valueDiff, -10**9), num + valueDiff + 1):
                if j in window and abs(i - window[j]) <= indexDiff:
                    return True
            window[num] = i
            if i >= indexDiff:
                del window[nums[i - indexDiff]]
        return False