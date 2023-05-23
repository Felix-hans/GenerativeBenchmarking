# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        numer = 0
        denom = 1

        fractions = expression.split('+')

        for fraction in fractions:
            if '-' in fraction:
                sign = -1
                fraction = fraction[1:]
            else:
                sign = 1

            num, den = map(int, fraction.split('/'))

            numer = numer * den + sign * num * denom
            denom *= den

        if numer == 0:
            return '0/1'

        divisor = gcd(numer, denom)
        numer //= divisor
        denom //= divisor

        return str(numer) + '/' + str(denom)