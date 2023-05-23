# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def expand_decimal(string):
            integer_part = ""
            non_repeating_part = ""
            repeating_part = ""
            
            if '.' in string:
                integer_part, decimal_part = string.split('.')
                
                if '(' in decimal_part:
                    non_repeating_part, repeating_part = decimal_part.split('(')
                    repeating_part = repeating_part[:-1]  # remove the closing parenthesis
                    
                else:
                    non_repeating_part = decimal_part
            
            else:
                integer_part = string
            
            return integer_part, non_repeating_part, repeating_part
        
        def convert_to_decimal(integer_part, non_repeating_part, repeating_part):
            decimal = float(integer_part)
            
            if non_repeating_part:
                decimal += float(non_repeating_part) / (10 ** len(non_repeating_part))
            
            if repeating_part:
                decimal += float(repeating_part) / ((10 ** len(non_repeating_part)) * (10 ** len(repeating_part) - 1))
            
            return decimal
        
        s_integer, s_non_repeating, s_repeating = expand_decimal(s)
        t_integer, t_non_repeating, t_repeating = expand_decimal(t)
        
        s_decimal = convert_to_decimal(s_integer, s_non_repeating, s_repeating)
        t_decimal = convert_to_decimal(t_integer, t_non_repeating, t_repeating)
        
        return s_decimal == t_decimal