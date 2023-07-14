# @lc app=leetcode id=2208 lang=python3
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        nums.sort(reverse=True)
        
        curr_sum = 0
        operations = 0
        for num in nums:
            curr_sum += num
            operations += 1
            if curr_sum >= total_sum / 2:
                break
                
        return operations