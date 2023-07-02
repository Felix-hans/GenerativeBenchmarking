# @lc app=leetcode id=843 lang=python3
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = len(words)
        guess_count = 0
        
        while guess_count < 10:
            char_freq = [[0] * 26 for _ in range(6)]
            for word in words:
                for i, char in enumerate(word):
                    char_freq[i][ord(char) - ord('a')] += 1
            
            min_elimination = float('inf')
            guess_word = ""
            for word in words:
                elimination_score = 0
                for i, char in enumerate(word):
                    elimination_score += char_freq[i][ord(char) - ord('a')]
                if elimination_score < min_elimination:
                    min_elimination = elimination_score
                    guess_word = word
            
            guess_result = master.guess(guess_word)
            guess_count += 1
            
            if guess_result == 6:
                print("You guessed the secret word correctly.")
                return
            
            filtered_words = []
            for word in words:
                match_count = sum(word[i] == guess_word[i] for i in range(6))
                if match_count == guess_result:
                    filtered_words.append(word)
            
            words = filtered_words
        
        print("Either you took too many guesses, or you did not find the secret word.")