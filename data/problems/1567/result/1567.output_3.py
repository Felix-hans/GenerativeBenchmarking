# @lc app=leetcode id=1567 lang=python3
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        neg_count = 0
        first_neg_idx = -1
        last_neg_idx = -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                neg_count += 1
                if first_neg_idx == -1:
                    first_neg_idx = i
                last_neg_idx = i
            elif nums[i] == 0:
                neg_count = 0
                first_neg_idx = -1
                last_neg_idx = -1
            else:
                if neg_count % 2 == 0:
                    max_len = max(max_len, i + 1)
                else:
                    max_len = max(max_len, i - first_neg_idx)
        
        return max_len