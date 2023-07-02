# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []  # current line words
        line_length = 0  # length of current line words without spaces
        
        for word in words:
            if line_length + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_length += len(word)
            else:
                result.append(self.justify_line(line, line_length, maxWidth))
                line = [word]
                line_length = len(word)
        
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
    
    def justify_line(self, line, line_length, maxWidth):
        if len(line) == 1 or len(line) + line_length == maxWidth:
            return ' '.join(line) + ' ' * (maxWidth - line_length - len(line) + 1)
        
        num_spaces = maxWidth - line_length
        num_gaps = len(line) - 1
        min_spaces = num_spaces // num_gaps
        extra_spaces = num_spaces % num_gaps
        
        justified_line = ''
        for i, word in enumerate(line):
            justified_line += word
            if i < num_gaps:
                spaces = min_spaces + (1 if i < extra_spaces else 0)
                justified_line += ' ' * spaces
        
        return justified_line