# @lc app=leetcode id=843 lang=python3
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = 0  # Number of calls to Master.guess()
        
        while n < 10:  # allowedGuesses is 10 in this case
            count = [0] * 6  # Count of each character position
            
            for word in words:
                for i, char in enumerate(word):
                    count[i] += ord(char) - ord('a')
            
            guess_word = max(words, key=lambda word: sum((char == guess_char) * -count[i] for i, char in enumerate(word)))
            matches = master.guess(guess_word)
            n += 1
            
            if matches == 6:
                print("You guessed the secret word correctly.")
                return
            
            words = [word for word in words if self.matchCount(word, guess_word) == matches]
        
        print("Either you took too many guesses, or you did not find the secret word.")
    
    def matchCount(self, word1: str, word2: str) -> int:
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 == c2:
                count += 1
        return count