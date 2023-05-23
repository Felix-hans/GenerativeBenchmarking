# @lc app=leetcode id=283 lang=python3
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_ptr = 0  # Pointer for the next non-zero element
        
        for curr_ptr in range(len(nums)):
            if nums[curr_ptr] != 0:
                nums[curr_ptr], nums[zero_ptr] = nums[zero_ptr], nums[curr_ptr]
                zero_ptr += 1