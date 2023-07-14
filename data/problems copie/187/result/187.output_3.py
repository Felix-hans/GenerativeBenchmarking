# @lc app=leetcode id=187 lang=python3
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()  # to store the unique 10-letter-long substrings
        repeated = set()  # to store the repeated 10-letter-long substrings

        for i in range(len(s) - 9):
            sequence = s[i:i+10]  # extract the current 10-letter-long substring

            if sequence in seen:
                repeated.add(sequence)
            else:
                seen.add(sequence)

        return list(repeated)