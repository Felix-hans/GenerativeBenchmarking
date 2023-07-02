# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_width = 0
        
        for word in words:
            if line_width + len(line) + len(word) <= maxWidth:
                line.append(word)
                line_width += len(word)
            else:
                result.append(self.format_line(line, maxWidth, line_width))
                line = [word]
                line_width = len(word)
        
        result.append(self.left_justify(line, maxWidth))
        return result
    
    def format_line(self, line, maxWidth, line_width):
        num_words = len(line)
        num_spaces = maxWidth - line_width
        if num_words == 1:
            return line[0] + ' ' * num_spaces
        
        space_slots = num_words - 1
        space_per_slot = num_spaces // space_slots
        extra_spaces = num_spaces % space_slots
        
        formatted_line = ''
        for i in range(len(line)):
            formatted_line += line[i]
            if i < space_slots:
                num_extra_spaces = extra_spaces if i < extra_spaces else 0
                formatted_line += ' ' * (space_per_slot + 1 + num_extra_spaces)
        
        return formatted_line
    
    def left_justify(self, line, maxWidth):
        formatted_line = ' '.join(line)
        formatted_line += ' ' * (maxWidth - len(formatted_line))
        return formatted_line