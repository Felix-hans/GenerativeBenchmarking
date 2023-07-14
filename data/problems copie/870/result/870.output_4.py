# @lc app=leetcode id=870 lang=python3
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2_sort = sorted([(num, i) for i, num in enumerate(nums2)])
        advantage = {}
        remaining = list(nums1)
        assigned = []
        
        for num, i in nums2_sort:
            if num < remaining[0]:
                advantage[i] = remaining[0]
                remaining.pop(0)
            else:
                assigned_num = next((n for n in remaining if n > num), remaining[0])
                advantage[i] = assigned_num
                remaining.remove(assigned_num)
                assigned.append(assigned_num)
        
        result = [advantage[i] if i in advantage else remaining.pop(0) for i in range(len(nums2))]
        return result