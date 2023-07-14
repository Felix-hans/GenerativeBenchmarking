# @lc app=leetcode id=843 lang=python3
from typing import List
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(word1: str, word2: str) -> int:
            count = 0
            for c1, c2 in zip(word1, word2):
                if c1 == c2:
                    count += 1
            return count

        def reduceWordsList(words: List[str], guess: str, matches: int) -> List[str]:
            return [word for word in words if match(word, guess) == matches]

        def getGuess(words: List[str]) -> str:
            return random.choice(words)

        guesses = 0
        while guesses < 10:
            guess = getGuess(words)
            matches = master.guess(guess)
            if matches == 6:
                print("You guessed the secret word correctly.")
                return
            words = reduceWordsList(words, guess, matches)
            guesses += 1

        print("Either you took too many guesses, or you did not find the secret word.")