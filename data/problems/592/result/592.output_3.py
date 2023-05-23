# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        numerator = 0
        denominator = 1

        fractions = expression.split('+')

        for fraction in fractions:
            if '-' in fraction:
                sign = -1
                fraction = fraction[1:]
            else:
                sign = 1

            num, denom = map(int, fraction.split('/'))
            numerator += sign * num * denominator
            denominator *= denom

        divisor = gcd(numerator, denominator)
        numerator //= divisor
        denominator //= divisor

        if denominator == 1:
            return str(numerator) + '/1'
        else:
            return str(numerator) + '/' + str(denominator)