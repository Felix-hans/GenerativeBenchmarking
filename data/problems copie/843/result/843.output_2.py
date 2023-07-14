# @lc app=leetcode id=843 lang=python3
from typing import List
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = 0  # Number of words in the wordlist
        while n < 6:
            guess_word = random.choice(words)  # Choose a random word as a guess
            matches = master.guess(guess_word)  # Get the number of matches for the guess
            if matches == 6:
                return  # Secret word found, end the function
            words = [word for word in words if self.matchCount(word, guess_word) == matches]  # Filter the remaining words based on the matches
            n += 1

    def matchCount(self, word1: str, word2: str) -> int:
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        return count