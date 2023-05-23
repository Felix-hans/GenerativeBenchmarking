# @lc app=leetcode id=1653 lang=python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0  # count of 'a' characters encountered so far
        deletions = 0  # number of deletions needed
        
        for char in s:
            if char == 'a':
                a_count += 1
            else:
                
                deletions += 1
                
                if a_count > 0:
                    a_count -= 1
                    deletions -= 1  # Undo the previous deletion of 'b'
        
        return deletions