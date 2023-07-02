# @lc app=leetcode id=592 lang=python3
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        fractions = expression.split('+')
        for fraction in fractions:
            if '-' in fraction:
                numerator_str, denominator_str = fraction.split('-')
                numerator -= int(numerator_str)
            else:
                numerator_str, denominator_str = fraction.split('/')
                numerator += int(numerator_str)

            current_denominator = int(denominator_str)
            lcm_val = self.lcm(denominator, current_denominator)
            numerator *= lcm_val // denominator
            numerator += int(numerator_str) * lcm_val // current_denominator
            denominator = lcm_val

        gcd_val = self.gcd(numerator, denominator)
        numerator //= gcd_val
        denominator //= gcd_val

        if denominator == 1:
            return str(numerator)
        else:
            return str(numerator) + '/' + str(denominator)