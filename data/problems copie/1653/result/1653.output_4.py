# @lc app=leetcode id=1653 lang=python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0  # Count of deletions needed to balance the string
        count_a = 0  # Count of 'a' characters encountered
        
        for char in s:
            if char == 'a':
                count_a += 1
            else:  # char == 'b'
                if count_a > 0:
                    count_a -= 1
                    deletions += 1
        
        return deletions