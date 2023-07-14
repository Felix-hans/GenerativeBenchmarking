# @lc app=leetcode id=843 lang=python3
import random
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        wordSet = set(words)
        guesses = 0

        while guesses < 10:
            guess = random.choice(list(wordSet))
            matches = master.guess(guess)

            if matches == 6:
                return "You guessed the secret word correctly."

            wordSet.remove(guess)
            wordSet = set(word for word in wordSet if self.matchCount(word, guess) == matches)

            guesses += 1

        return "Either you took too many guesses, or you did not find the secret word."

    def matchCount(self, word1: str, word2: str) -> int:
        return sum(c1 == c2 for c1, c2 in zip(word1, word2))