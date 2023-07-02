# @lc app=leetcode id=68 lang=python3
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # List to store the formatted lines
        curr_line = []  # List to store the words of the current line
        curr_width = 0  # Current width of the line (sum of word lengths)

        for word in words:
            if curr_width + len(curr_line) + len(word) > maxWidth:
                num_spaces = maxWidth - curr_width

                if len(curr_line) == 1:
                    line = curr_line[0] + ' ' * num_spaces
                else:
                    space_between_words = num_spaces // (len(curr_line) - 1)
                    extra_spaces = num_spaces % (len(curr_line) - 1)

                    line = ''
                    for i in range(len(curr_line) - 1):
                        line += curr_line[i] + ' ' * space_between_words
                        if extra_spaces > 0:
                            line += ' '
                            extra_spaces -= 1
                    line += curr_line[-1]  # Add the last word without extra spaces

                result.append(line)  # Add the formatted line to the result

                curr_line = []  # Clear the current line
                curr_width = 0  # Reset the current width

            curr_line.append(word)  # Add the word to the current line
            curr_width += len(word)  # Update the current width

        last_line = ' '.join(curr_line)
        last_line += ' ' * (maxWidth - len(last_line))  # Add extra spaces at the end
        result.append(last_line)

        return result