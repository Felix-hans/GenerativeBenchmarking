# @lc app=leetcode id=819 lang=python3
from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        words = paragraph.split()
        
        word_count = Counter(words)
        
        max_count = 0
        most_common_word = ''
        
        for word, count in word_count.items():
            if word not in banned and count > max_count:
                max_count = count
                most_common_word = word
        
        return most_common_word