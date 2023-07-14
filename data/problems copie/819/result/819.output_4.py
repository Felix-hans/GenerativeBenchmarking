# @lc app=leetcode id=819 lang=python3
from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z0-9]', ' ', paragraph.lower())
        
        words = paragraph.split()
        
        word_count = Counter(words)
        
        for word in banned:
            word_count[word] = 0
        
        most_common = word_count.most_common(1)
        
        return most_common[0][0]