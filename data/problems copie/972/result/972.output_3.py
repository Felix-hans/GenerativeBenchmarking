# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse_number(string):
            integer_part = ''
            non_repeating_part = ''
            repeating_part = ''
            decimal_found = False
            repeating_found = False

            i = 0
            while i < len(string):
                if string[i] == '.':
                    decimal_found = True
                    i += 1
                elif string[i] == '(':
                    repeating_found = True
                    i += 1
                elif string[i] == ')':
                    i += 1
                elif repeating_found:
                    repeating_part += string[i]
                    i += 1
                elif decimal_found:
                    non_repeating_part += string[i]
                    i += 1
                else:
                    integer_part += string[i]
                    i += 1

            return integer_part, non_repeating_part, repeating_part

        s_int, s_non_repeating, s_repeating = parse_number(s)
        t_int, t_non_repeating, t_repeating = parse_number(t)

        max_repeating_length = max(len(s_repeating), len(t_repeating))
        s_repeating = s_repeating.ljust(max_repeating_length, '0')
        t_repeating = t_repeating.ljust(max_repeating_length, '0')

        s_number = s_int + s_non_repeating + s_repeating
        t_number = t_int + t_non_repeating + t_repeating

        return float(s_number) == float(t_number)