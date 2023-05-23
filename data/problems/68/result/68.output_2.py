# @lc app=leetcode id=68 lang=python3
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        current_line = []
        current_width = 0

        for word in words:
            if current_width + len(current_line) + len(word) <= maxWidth:
                current_line.append(word)
                current_width += len(word)
            else:
                num_words = len(current_line)
                num_spaces = maxWidth - current_width

                if num_words == 1:
                    line = current_line[0] + ' ' * num_spaces
                else:
                    spaces_between_words = num_spaces // (num_words - 1)
                    extra_spaces = num_spaces % (num_words - 1)

                    line = ''
                    for i in range(num_words - 1):
                        line += current_line[i] + ' ' * spaces_between_words
                        if i < extra_spaces:
                            line += ' '
                    line += current_line[-1]  # Add the last word

                result.append(line)

                current_line = [word]
                current_width = len(word)

        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result