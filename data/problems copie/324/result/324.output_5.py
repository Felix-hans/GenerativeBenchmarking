# @lc app=leetcode id=324 lang=python3
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums.sort()
        result = [0] * n
        small = (n + 1) // 2
        large = n
        
        for i in range(n):
            if i % 2 == 1:
                result[i] = nums[small]
                small -= 1
            else:
                result[i] = nums[large]
                large -= 1
        
        nums[:] = result  # Modify nums in-place