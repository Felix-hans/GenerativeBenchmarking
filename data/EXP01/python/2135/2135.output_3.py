# @lc app=leetcode id=2135 lang=python3
from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        freqArray = [[0] * 26 for _ in range(len(startWords[0]))]
        
        for word in startWords:
            for i, char in enumerate(word):
                freqArray[i][ord(char) - ord('a')] += 1
        
        count = 0
        for word in targetWords:
            for i, char in enumerate(word):
                freqArray[i][ord(char) - ord('a')] -= 1
                if freqArray[i][ord(char) - ord('a')] < 0:
                    break
            else:
                count += 1
        
        return count