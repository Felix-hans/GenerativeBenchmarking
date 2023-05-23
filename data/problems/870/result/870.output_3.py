# @lc app=leetcode id=870 lang=python3
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        result = [-1] * len(nums1)
        remaining_nums1 = []

        j = 0
        for num2 in sorted_nums2:
            if sorted_nums1[j] > num2:
                result[nums2.index(num2)] = sorted_nums1[j]
                j += 1
            else:
                remaining_nums1.append(sorted_nums1[j])
                j += 1

        for i in range(len(result)):
            if result[i] == -1:
                result[i] = remaining_nums1.pop()

        return result