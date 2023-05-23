# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(string):
            if '.' not in string:
                return int(string)
            
            integer_part, decimal_part = string.split('.')
            non_repeating_part, repeating_part = '', ''
            
            if '(' in decimal_part:
                decimal_part, repeating_part = decimal_part.split('(')
                repeating_part = repeating_part[:-1]  # Remove the closing bracket
            
            return float(integer_part + '.' + decimal_part + repeating_part * 10)
        
        s_decimal = convert_to_decimal(s)
        t_decimal = convert_to_decimal(t)
        
        return s_decimal == t_decimal