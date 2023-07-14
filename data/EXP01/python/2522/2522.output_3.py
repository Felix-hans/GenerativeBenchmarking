# @lc app=leetcode id=2522 lang=python3
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        curr_value = 0

        for digit in s:
            curr_value = curr_value * 10 + int(digit)
            if curr_value > k:
                return -1
            if curr_value == k:
                count += 1
                curr_value = 0
                continue
            if curr_value > 0:
                count += 1
                curr_value = int(digit)

        if curr_value > 0:
            count += 1

        return count