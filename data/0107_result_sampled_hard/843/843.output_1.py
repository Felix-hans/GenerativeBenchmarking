# @lc app=leetcode id=843 lang=python3
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = 6  # Length of each word
        
        def matchCount(word1, word2):
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))
        
        def minimizeWords():
            candidates = set(range(len(words)))

            for _ in range(10):  # Maximum 10 allowed guesses
                guess = next(iter(candidates))  # Choose a random candidate
                matches = master.guess(words[guess])
                if matches == n:  # Found the secret word
                    return
                candidates = {c for c in candidates if matchCount(words[guess], words[c]) == matches}

        minimizeWords()