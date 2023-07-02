# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(string):
            if '(' in string:
                integer, decimal = string.split('.')
                non_repeating_part, repeating_part = decimal.split('(')
                
                repeating_length = len(repeating_part) - 1
                
                combined_part = non_repeating_part + repeating_part[:-1]
                
                decimal_value = int(combined_part) / (10 ** len(non_repeating_part))
                
                repeating_value = int(repeating_part) / (10 ** len(non_repeating_part)) / (10 ** repeating_length)
                
                decimal_value += repeating_value
                
                return decimal_value
            
            return float(string)
        
        decimal_s = convert_to_decimal(s)
        decimal_t = convert_to_decimal(t)
        
        return decimal_s == decimal_t