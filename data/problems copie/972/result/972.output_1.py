# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def convert_to_float(string: str) -> float:
            if '(' in string:
                non_repeating_part, repeating_part = string.split('(')
                repeating_part = repeating_part[:-1]  # Remove the closing parenthesis
                decimal_part = non_repeating_part + repeating_part * 100  # Multiply by a large number to expand the repeating part
            else:
                decimal_part = string

            return float(decimal_part)

        return convert_to_float(s) == convert_to_float(t)