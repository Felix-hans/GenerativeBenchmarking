# @lc app=leetcode id=870 lang=python3
class Solution:
    def advantageCount(self, nums1, nums2):
        nums1.sort()
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: x[1])
        result = [0] * len(nums1)
        left, right = 0, len(nums2) - 1

        for num in reversed(nums1):
            index, value = sorted_nums2[right]
            if num > value:
                result[index] = num
                right -= 1
            else:
                index, value = sorted_nums2[left]
                result[index] = num
                left += 1

        return result