# @lc app=leetcode id=592 lang=python3
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        fractions = expression.split('+')
        for fraction in fractions:
            if '-' in fraction:
                num, denom = fraction.split('-')
                sign = -1
            else:
                num, denom = fraction.split('+')
                sign = 1

            num = int(num)
            denom = int(denom)
            numerator = numerator * denom + sign * num * denominator
            denominator *= denom

        gcd = self.gcd(abs(numerator), denominator)
        numerator //= gcd
        denominator //= gcd

        return str(numerator) + '/' + str(denominator)