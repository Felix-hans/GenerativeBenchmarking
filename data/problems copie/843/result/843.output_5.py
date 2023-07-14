# @lc app=leetcode id=843 lang=python3
import random
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        candidates = set(words)
        allowedGuesses = 10

        while candidates and allowedGuesses > 0:
            guess = random.choice(list(candidates))
            matches = master.guess(guess)
            allowedGuesses -= 1

            if matches == len(guess):
                return "You guessed the secret word correctly."

            candidates = {word for word in candidates if self.countMatches(guess, word) == matches}

        return "Either you took too many guesses, or you did not find the secret word."

    def countMatches(self, word1: str, word2: str) -> int:
        return sum(c1 == c2 for c1, c2 in zip(word1, word2))