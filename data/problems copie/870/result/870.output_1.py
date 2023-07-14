# @lc app=leetcode id=870 lang=python3
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # Sort nums1 in ascending order
        sorted_nums2 = sorted(enumerate(nums2), key=lambda x: x[1])  # Sort nums2 and keep track of the original indices

        result = [-1] * len(nums1)  # Initialize the result array with -1
        low, high = 0, len(nums1) - 1  # Pointers for nums1

        for i, num in sorted_nums2:
            if nums1[high] > num:
                result[i] = nums1[high]
                high -= 1
            else:
                result[i] = nums1[low]
                low += 1

        return result