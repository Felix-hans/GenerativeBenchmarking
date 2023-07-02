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
            parts = fraction.split('/')
            num = int(parts[0])
            denom = int(parts[1])

            if '-' in parts[0]:
                num *= -1

            common_denominator = denominator * denom
            numerator = numerator * denom + num * denominator
            denominator = common_denominator

        if numerator == 0:
            return '0/1'

        divisor = gcd(abs(numerator), denominator)
        numerator //= divisor
        denominator //= divisor

        return str(numerator) + '/' + str(denominator)