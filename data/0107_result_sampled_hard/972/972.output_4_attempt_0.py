# @lc app=leetcode id=972 lang=python3
class Solution:
    def get_decimal_value(self, decimal_part: str) -> float:
        value = 0
        power = 0
        for digit in decimal_part:
            value += int(digit) * 10 ** (-power)
            power += 1
        return value

    def isRationalEqual(self, s: str, t: str) -> bool:
        s_integer, s_non_repeating, s_repeating = self.split_rational_number(s)
        t_integer, t_non_repeating, t_repeating = self.split_rational_number(t)

        if s_integer != t_integer:
            return False

        if s_non_repeating != t_non_repeating:
            s_non_repeating_value = self.get_decimal_value(s_non_repeating)
            t_non_repeating_value = self.get_decimal_value(t_non_repeating)
            if s_non_repeating_value != t_non_repeating_value:
                return False

        if s_repeating and t_repeating:
            s_repeating_value = self.get_decimal_value(s_repeating)
            t_repeating_value = self.get_decimal_value(t_repeating)
            if s_repeating_value != t_repeating_value:
                return False

        return True

    def split_rational_number(self, number: str) -> tuple:
        integer_part = ""
        non_repeating_part = ""
        repeating_part = ""

        if "." in number:
            parts = number.split(".")
            integer_part = parts[0]
            if "(" in parts[1]:
                non_repeating_part, repeating_part = parts[1].split("(")
                repeating_part = repeating_part[:-1]  # Remove the closing bracket ")"
            else:
                non_repeating_part = parts[1]

        return integer_part, non_repeating_part, repeating_part