# @lc app=leetcode id=843 lang=python3
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        allowedGuesses = 10
        
        wordSet = set(words)
        matched = 0
        
        while allowedGuesses > 0:
            count = {ch: 0 for ch in "abcdef"}
            for word in words:
                for ch in word:
                    count[ch] += 1
            
            words.sort(key=lambda w: sum(count[ch] for ch in w))
            guessedWord = words.pop()
            matched = master.guess(guessedWord)
            
            if matched == len(guessedWord):
                return "You guessed the secret word correctly."
            
            allowedGuesses -= 1
            words = [word for word in words if self.countMatches(word, guessedWord) == matched]
        
        return "Either you took too many guesses, or you did not find the secret word."
    
    def countMatches(self, word1: str, word2: str) -> int:
        return sum(ch1 == ch2 for ch1, ch2 in zip(word1, word2))