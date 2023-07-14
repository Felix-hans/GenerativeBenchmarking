# @lc app=leetcode id=788 lang=python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        for num in range(1, n+1):
            if any(digit in {3, 4, 7} for digit in map(int, str(num))):
                continue
            
            if any(digit in {2, 5, 6, 9} for digit in map(int, str(num))):
                count += 1
        
        return count