# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        current_line = []  # List to store words in the current line
        current_width = 0  # Width of the current line

        for word in words:
            if current_width + len(current_line) + len(word) <= maxWidth:
                current_line.append(word)
                current_width += len(word)
            else:
                result.append(self.justify_line(current_line, maxWidth))
                current_line = [word]
                current_width = len(word)

        last_line = ' '.join(current_line)
        last_line = last_line.ljust(maxWidth)  # Left-justify the last line
        result.append(last_line)

        return result

    def justify_line(self, line, maxWidth):
        if len(line) == 1:
            return line[0].ljust(maxWidth)  # Left-justify if only one word in the line

        num_spaces = maxWidth - sum(len(word) for word in line)
        num_gaps = len(line) - 1

        if num_gaps == 0:
            spaces_per_gap = num_spaces
            extra_spaces = 0
        else:
            spaces_per_gap = num_spaces // num_gaps
            extra_spaces = num_spaces % num_gaps

        justified_line = ''
        for i in range(len(line) - 1):
            justified_line += line[i] + ' ' * spaces_per_gap
            if extra_spaces > 0:
                justified_line += ' '
                extra_spaces -= 1

        justified_line += line[-1]  # Add the last word without any spaces

        return justified_line.ljust(maxWidth)  # Left-justify the line