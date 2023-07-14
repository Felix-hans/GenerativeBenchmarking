# @lc app=leetcode id=187 lang=python3
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)  # Store the count of each 10-letter sequence
        result = []
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]  # Get the current 10-letter sequence
            
            sequences[sequence] += 1
            
            if sequences[sequence] == 2:
                result.append(sequence)
        
        return result