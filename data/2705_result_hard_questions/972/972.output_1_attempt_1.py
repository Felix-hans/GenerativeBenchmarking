# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def expand_decimal(s):
            integer_part, decimal_part = s.split('.')
            non_repeating_part = ''
            repeating_part = ''

            if '(' in decimal_part:
                non_repeating_part, repeating_part = decimal_part.split('(')
                repeating_part = repeating_part[:-1]
            else:
                non_repeating_part = decimal_part

            return integer_part, non_repeating_part, repeating_part

        def generate_decimal(integer_part, non_repeating_part, repeating_part, precision):
            decimal_expansion = integer_part + '.' + non_repeating_part

            if repeating_part:
                decimal_expansion += repeating_part * precision

            return decimal_expansion

        s_integer, s_non_repeating, s_repeating = expand_decimal(s)
        t_integer, t_non_repeating, t_repeating = expand_decimal(t)

        precision = 10 ** 5
        s_decimal = generate_decimal(s_integer, s_non_repeating, s_repeating, precision)
        t_decimal = generate_decimal(t_integer, t_non_repeating, t_repeating, precision)

        return s_decimal == t_decimal