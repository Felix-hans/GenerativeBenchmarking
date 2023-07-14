# @lc app=leetcode id=843 lang=python3
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def get_matches(word1: str, word2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        def remove_word(word: str, possible: set):
            possible.discard(word)

        possible = set(words)
        guesses = 0

        while possible and guesses < 10:
            guess = possible.pop()
            matches = master.guess(guess)
            if matches == 6:
                return "You guessed the secret word correctly."
            possible = {word for word in possible if get_matches(guess, word) == matches}
            guesses += 1

        return "Either you took too many guesses, or you did not find the secret word."