# @lc app=leetcode id=324 lang=python3
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        nums.sort()
        
        mid = n // 2
        nums1 = nums[:mid]
        nums2 = nums[mid:]
        
        new_nums = [0] * n
        
        j = 0
        for i in range(n-1, 0, -2):
            new_nums[i] = nums2[j]
            j += 1
        for i in range(1, n, 2):
            new_nums[i] = nums1[j]
            j += 1
        
        for i in range(n):
            nums[i] = new_nums[i]