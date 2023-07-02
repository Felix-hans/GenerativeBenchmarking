# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        numerator = 0
        denominator = 1

        fractions = expression.split('+')
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            lcm = denominator * denom // gcd(denominator, denom)
            numerator = numerator * (lcm // denominator) + num * (lcm // denom)
            denominator = lcm

        gcd_val = gcd(abs(numerator), denominator)
        numerator //= gcd_val
        denominator //= gcd_val

        return str(numerator) + '/' + str(denominator)