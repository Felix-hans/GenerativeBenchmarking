# @lc app=leetcode id=1653 lang=python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0  # variable to count the deletions
        b_count = 0  # variable to count the number of 'b's after each 'a'

        for char in s:
            if char == 'a':
                deletions = min(deletions + 1, b_count)
            else:
                b_count += 1

        return deletions