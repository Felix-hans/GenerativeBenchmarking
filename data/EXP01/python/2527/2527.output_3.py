# @lc app=leetcode id=2527 lang=python3
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    effective_value = (nums[i] | nums[j]) & nums[k]
                    result ^= effective_value
        
        return result