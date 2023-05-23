# @lc app=leetcode id=68 lang=python3
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        current_width = 0
        
        for word in words:
            if current_width + len(current_line) + len(word) > maxWidth:
                num_spaces = maxWidth - current_width
                if len(current_line) > 1:
                    space_between_words = num_spaces // (len(current_line) - 1)
                    extra_spaces = num_spaces % (len(current_line) - 1)
                    formatted_line = ''
                    for i in range(len(current_line) - 1):
                        formatted_line += current_line[i] + ' ' * space_between_words
                        if extra_spaces > 0:
                            formatted_line += ' '
                            extra_spaces -= 1
                    formatted_line += current_line[-1]  # Add the last word
                else:
                    formatted_line = current_line[0] + ' ' * num_spaces
                
                result.append(formatted_line)
                current_line = [word]
                current_width = len(word)
            else:
                current_line.append(word)
                current_width += len(word)
        
        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result