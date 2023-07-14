# @lc app=leetcode id=1653 lang=python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0  # Variable to store the number of deletions needed
        a_count = 0  # Variable to count 'a' characters
        
        for char in s:
            if char == 'a':
                a_count += 1
            else:
                deletions += min(1, a_count)
        
        return deletions