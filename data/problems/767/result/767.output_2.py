# @lc app=leetcode id=767 lang=python3
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        result = []

        while counter:
            char, freq = counter.most_common(1)[0]
            counter[char] -= 1

            if result and result[-1] == char:
                return ""

            result.append(char)

            if counter[char] == 0:
                del counter[char]

        return "".join(result)