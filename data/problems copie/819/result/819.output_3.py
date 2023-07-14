# @lc app=leetcode id=819 lang=python3
from typing import List
import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())

        word_counts = Counter(word for word in words if word not in banned)

        most_common_word = word_counts.most_common(1)[0][0]

        return most_common_word