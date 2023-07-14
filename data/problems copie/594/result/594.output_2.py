# @lc app=leetcode id=594 lang=python3
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_freq = {}
        max_length = 0
        
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        for num in num_freq:
            if num + 1 in num_freq:
                subseq_length = num_freq[num] + num_freq[num + 1]
                max_length = max(max_length, subseq_length)
        
        return max_length