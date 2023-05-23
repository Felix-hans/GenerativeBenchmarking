# @lc app=leetcode id=1653 lang=python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0  # Count of deletions needed
        b_count = 0    # Count of 'b's encountered
        
        for char in s:
            if char == 'a':
                if b_count > 0:
                    deletions += 1
                    b_count -= 1
            else:
                b_count += 1
        
        return deletions