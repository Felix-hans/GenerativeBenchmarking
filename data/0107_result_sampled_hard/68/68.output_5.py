# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []  # Store the final formatted lines
        
        i = 0
        while i < len(words):
            line_words = []  # Words for the current line
            line_width = 0  # Total width of the words in the line
            
            while i < len(words) and line_width + len(line_words) + len(words[i]) <= maxWidth:
                line_words.append(words[i])
                line_width += len(words[i])
                i += 1
            
            line = ''  # Formatted line string
            
            if i == len(words) or len(line_words) == 1:
                line = ' '.join(line_words)  # Left-justified line
                line += ' ' * (maxWidth - line_width - len(line_words) + 1)  # Add spaces to reach maxWidth
            else:
                num_spaces = maxWidth - line_width  # Total number of spaces to distribute
                num_gaps = len(line_words) - 1  # Number of gaps between words
                
                spaces_per_gap = num_spaces // num_gaps
                extra_spaces = num_spaces % num_gaps
                
                for j in range(len(line_words) - 1):
                    line += line_words[j]
                    line += ' ' * spaces_per_gap
                    if extra_spaces > 0:
                        line += ' '
                        extra_spaces -= 1
                
                line += line_words[-1]  # Add the last word
                
            result.append(line)
        
        return result