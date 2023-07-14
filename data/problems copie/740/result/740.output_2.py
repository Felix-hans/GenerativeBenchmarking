# @lc app=leetcode id=740 lang=python3
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        
        max_points = [0] * (max(nums) + 1)
        
        max_points[1] = freq[1] * 1  # If the array contains only 1, earn its points
        max_points[2] = max(max_points[1], freq[2] * 2)  # Compare earning 2 or keeping 1
        
        for i in range(3, len(max_points)):
            max_points[i] = max(max_points[i-1], max_points[i-2] + freq[i] * i)
        
        return max_points[-1]