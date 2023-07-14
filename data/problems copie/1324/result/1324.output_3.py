# @lc app=leetcode id=1324 lang=python3
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()  # Split the string into individual words
        max_length = max(len(word) for word in words)  # Find the maximum length among all words
        
        result = []
        for i in range(max_length):
            vertical_word = ""
            for word in words:
                if i < len(word):
                    vertical_word += word[i]
                else:
                    vertical_word += " "
            
            vertical_word = vertical_word.rstrip()  # Remove trailing spaces
            result.append(vertical_word)
        
        return result