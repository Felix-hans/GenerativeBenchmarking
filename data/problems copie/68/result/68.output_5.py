# @lc app=leetcode id=68 lang=python3
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # Store the formatted lines
        
        line_words = []  # Words in the current line
        line_length = 0  # Total length of characters in the line
        
        for word in words:
            if line_length + len(line_words) + len(word) > maxWidth:
                num_words = len(line_words)
                num_spaces = maxWidth - line_length
                
                if num_words == 1:
                    formatted_line = line_words[0] + ' ' * num_spaces
                else:
                    spaces_between_words = num_spaces // (num_words - 1)
                    extra_spaces = num_spaces % (num_words - 1)
                    
                    formatted_line = ''
                    for i in range(num_words - 1):
                        formatted_line += line_words[i] + ' ' * spaces_between_words
                        if i < extra_spaces:
                            formatted_line += ' '
                    formatted_line += line_words[-1]  # Add the last word
                
                result.append(formatted_line)  # Add the formatted line to the result
                
                line_words = []
                line_length = 0
            
            line_words.append(word)
            line_length += len(word)
        
        last_line = ' '.join(line_words)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result