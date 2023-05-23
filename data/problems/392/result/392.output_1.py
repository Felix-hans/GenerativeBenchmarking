# @lc app=leetcode id=392 lang=python3
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indices = defaultdict(list)  # store the indices of characters in t
        for i, ch in enumerate(t):
            indices[ch].append(i)

        j = 0  # index for t
        for ch in s:
            if ch not in indices:
                return False
            next_idx_list = indices[ch]
            left, right = 0, len(next_idx_list) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if next_idx_list[mid] > j:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(next_idx_list):
                return False
            j = next_idx_list[left] + 1

        return True