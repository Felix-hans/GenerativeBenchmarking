# @lc app=leetcode id=1567 lang=python3
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0  # Maximum length of subarray with positive product
        neg_count = 0  # Number of negative elements in the current subarray
        first_neg = -1  # Index of the first negative element in the current subarray

        for i in range(len(nums)):
            if nums[i] == 0:
                neg_count = 0
                first_neg = -1
            elif nums[i] < 0:
                neg_count += 1
                if first_neg == -1:
                    first_neg = i
            if neg_count % 2 == 0:
                max_len = max(max_len, i + 1)
            else:
                max_len = max(max_len, i - first_neg)

        return max_len