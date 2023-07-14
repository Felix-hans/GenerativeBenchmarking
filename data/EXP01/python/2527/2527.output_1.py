# @lc app=leetcode id=2527 lang=python3
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result ^= (nums[i] | nums[j]) & nums[k]
        
        return result