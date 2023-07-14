# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse_number(num_str):
            integer_part = 0
            non_repeating_part = 0
            repeating_part = 0
            repeating_length = 0
            repeating_started = False

            if '.' in num_str:
                integer_part, num_str = num_str.split('.', 1)
            
            if '(' in num_str:
                non_repeating_part, num_str = num_str.split('(', 1)
                num_str, repeating_part = num_str.split(')', 1)
                repeating_length = len(repeating_part)
                repeating_started = True

            non_repeating_part += num_str

            integer_part = int(integer_part)
            non_repeating_part = int(non_repeating_part)
            repeating_part = int(repeating_part) if repeating_started else 0

            return integer_part, non_repeating_part, repeating_part, repeating_length
        
        s_int, s_non_repeating, s_repeating, s_length = parse_number(s)
        t_int, t_non_repeating, t_repeating, t_length = parse_number(t)
        
        s_decimal = s_int + s_non_repeating / (10 ** len(str(s_non_repeating)))
        if s_repeating > 0:
            s_decimal += s_repeating / (10 ** s_length) / (10 ** len(str(s_non_repeating)))
        
        t_decimal = t_int + t_non_repeating / (10 ** len(str(t_non_repeating)))
        if t_repeating > 0:
            t_decimal += t_repeating / (10 ** t_length) / (10 ** len(str(t_non_repeating)))

        return s_decimal == t_decimal