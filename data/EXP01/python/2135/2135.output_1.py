# @lc app=leetcode id=2135 lang=python3
from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        count = 0
        
        for target in targetWords:
            target_freq = [0] * 26
            
            for ch in target:
                target_freq[ord(ch) - ord('a')] += 1
            
            for start in startWords:
                start_freq = [0] * 26
                
                for ch in start:
                    start_freq[ord(ch) - ord('a')] += 1
                
                is_transformable = True
                for i in range(26):
                    if start_freq[i] > target_freq[i]:
                        is_transformable = False
                        break
                
                if is_transformable:
                    count += 1
                    break
        
        return count