# @lc app=leetcode id=2208 lang=python3
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        nums.sort(reverse=True)
        target = total_sum / 2
        operations = 0
        
        for num in nums:
            if num <= target:
                break
            target /= 2
            operations += 1
            
        return operations