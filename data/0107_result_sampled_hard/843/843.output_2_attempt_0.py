# @lc app=leetcode id=843 lang=python3
from typing import List
import random

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master', allowedGuesses: int) -> None:
        possible_words = set(words)
        
        for _ in range(allowedGuesses):
            guess = random.choice(list(possible_words))
            matches = master.guess(guess)
            
            if matches == -1:
                possible_words.remove(guess)
            elif matches == 6:
                return "You guessed the secret word correctly."
            else:
                possible_words = {word for word in possible_words if self.matchCount(word, guess) == matches}
        
        return "Either you took too many guesses, or you did not find the secret word."
    
    def matchCount(self, word1: str, word2: str) -> int:
        count = 0
        for ch1, ch2 in zip(word1, word2):
            if ch1 == ch2:
                count += 1
        return count