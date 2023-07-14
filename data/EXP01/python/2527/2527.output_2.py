# @lc app=leetcode id=2527 lang=python3
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        xor_beauty = 0
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    effective_val = (nums[i] | nums[j]) & nums[k]
                    xor_beauty ^= effective_val
                    
        return xor_beauty