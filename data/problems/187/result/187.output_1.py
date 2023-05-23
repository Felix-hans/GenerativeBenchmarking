# @lc app=leetcode id=187 lang=python3
from collections import Counter
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        
        sequences = []
        counter = Counter()
        
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            counter[sequence] += 1
            if counter[sequence] == 2:
                sequences.append(sequence)
        
        return sequences