# @lc app=leetcode id=2135 lang=python3
from collections import Counter
from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        count_start = [Counter(word) for word in startWords]
        count_target = [Counter(word) for word in targetWords]
        
        result = 0
        for i in range(len(targetWords)):
            found = False
            for j in range(len(startWords)):
                if all(count_target[i][c] <= count_start[j][c] for c in count_target[i]):
                    found = True
                    break
            if found:
                result += 1
        
        return result