# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        curr_line = []
        curr_width = 0
        
        for word in words:
            if curr_width + len(curr_line) + len(word) <= maxWidth:
                curr_line.append(word)
                curr_width += len(word)
            else:
                result.append(self.justify_line(curr_line, curr_width, maxWidth))
                curr_line = [word]
                curr_width = len(word)
        
        last_line = ' '.join(curr_line)
        last_line = last_line.ljust(maxWidth)
        result.append(last_line)
        
        return result
    
    def justify_line(self, words, curr_width, maxWidth):
        num_words = len(words)
        num_spaces = maxWidth - curr_width
        if num_words == 1:
            return words[0].ljust(maxWidth)
        
        spaces_between_words = num_spaces // (num_words - 1)
        extra_spaces = num_spaces % (num_words - 1)
        
        justified_line = ''
        for i in range(num_words - 1):
            justified_line += words[i] + ' ' * spaces_between_words
            if i < extra_spaces:
                justified_line += ' '
        
        justified_line += words[num_words - 1]
        
        return justified_line