# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_width = 0
        word_count = len(words)
        index = 0
        
        while index < word_count:
            if line_width + len(words[index]) + len(line) <= maxWidth:
                line.append(words[index])
                line_width += len(words[index])
                index += 1
            else:
                result.append(self.justify_line(line, maxWidth, False))
                line = []
                line_width = 0
        
        result.append(self.justify_line(line, maxWidth, True))
        
        return result
    
    def justify_line(self, line, maxWidth, is_last_line):
        if len(line) == 1 or is_last_line:
            return ' '.join(line).ljust(maxWidth)
        
        total_width = sum(len(word) for word in line)
        total_spaces = maxWidth - total_width
        spaces_between_words = total_spaces // (len(line) - 1)
        extra_spaces = total_spaces % (len(line) - 1)
        
        justified_line = ''
        for i in range(len(line) - 1):
            justified_line += line[i] + ' ' * spaces_between_words
            if i < extra_spaces:
                justified_line += ' '  # Distribute extra spaces
            
        justified_line += line[-1]  # Add the last word
        
        return justified_line