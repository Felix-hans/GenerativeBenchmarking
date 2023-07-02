# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(num_str):
            integer_part, decimal_part = num_str.split('.')
            decimal_value = int(integer_part)
            
            if decimal_part.startswith('('):  # Repeating part exists
                repeating_part = decimal_part[1:-1]
                non_repeating_part = decimal_part[:decimal_part.index('(')]
                
                decimal_value += int(non_repeating_part)
                decimal_value += int(repeating_part) / (10 ** len(non_repeating_part))
                decimal_value += int(repeating_part) / (10 ** (len(non_repeating_part) + len(repeating_part)))  # To account for repeating part
                
            else:  # Only non-repeating part exists
                decimal_value += int(decimal_part) / (10 ** len(decimal_part))
            
            return decimal_value
        
        decimal_s = convert_to_decimal(s)
        decimal_t = convert_to_decimal(t)
        
        return decimal_s == decimal_t