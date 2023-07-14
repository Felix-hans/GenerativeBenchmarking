# @lc app=leetcode id=68 lang=python3
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # to store the formatted lines
        
        line = ""  # current line being constructed
        line_length = 0  # length of the current line
        
        for i, word in enumerate(words):
            if line_length + len(word) + len(line) > maxWidth:
                
                if len(line.split()) == 1:
                    line += " " * (maxWidth - line_length)
                else:
                    total_spaces = maxWidth - line_length
                    spaces_between_words = total_spaces // (len(line.split()) - 1)
                    extra_spaces = total_spaces % (len(line.split()) - 1)
                    
                    line = line.replace(" ", " " * spaces_between_words)
                    
                    line = line.replace(" " * spaces_between_words, " " * (spaces_between_words + 1), extra_spaces)
                
                result.append(line)  # add the justified line to the result
                line = ""  # reset line for the next line
                line_length = 0  # reset line_length for the next line
            
            line += word + " "  # add the word to the line
            line_length += len(word) + 1  # update the line_length
        
        line += " " * (maxWidth - line_length)
        result.append(line)
        
        return result