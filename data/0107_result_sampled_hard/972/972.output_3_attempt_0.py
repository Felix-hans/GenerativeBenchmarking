# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_decimal(num_str: str) -> float:
            decimal_str = num_str.replace('(', '').replace(')', '')  # Remove parentheses if present
            repeating_part = ''
            if '(' in num_str:  # Check if there is a repeating part
                non_repeating_part, repeating_part = decimal_str.split('.')
                decimal_str = non_repeating_part + repeating_part * 10  # Repeat the non-repeating part

            return float(decimal_str)

        decimal_s = convert_to_decimal(s)
        decimal_t = convert_to_decimal(t)

        return decimal_s == decimal_t