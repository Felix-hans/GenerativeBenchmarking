# @lc app=leetcode id=870 lang=python3
class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        sorted_nums2 = sorted(nums2)
        remaining = []
        
        left = 0
        right = 0
        
        while left < len(nums1) and right < len(nums2):
            if nums1[left] > sorted_nums2[right]:
                nums1[left], sorted_nums2[right] = sorted_nums2[right], nums1[left]
                left += 1
                right += 1
            else:
                remaining.append(nums1[left])
                left += 1
        
        result = []
        
        for num in nums2:
            index = bisect.bisect_right(sorted_nums2, num)
            if index < len(sorted_nums2):
                result.append(sorted_nums2[index])
                sorted_nums2.pop(index)
            else:
                result.append(remaining.pop())
        
        return result