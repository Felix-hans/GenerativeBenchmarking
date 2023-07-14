# @lc app=leetcode id=338 lang=python3
class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)  # Initialize the result array with zeros
        
        for i in range(1, n + 1):
            bits[i] = bits[i // 2] + (i % 2)
        
        return bits