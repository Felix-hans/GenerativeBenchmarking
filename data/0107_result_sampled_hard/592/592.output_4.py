# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        numerator = 0
        denominator = 1

        fractions = []
        current_fraction = ""
        for char in expression:
            if char == '+' or char == '-':
                if current_fraction:
                    fractions.append(current_fraction)
                current_fraction = char
            else:
                current_fraction += char
        fractions.append(current_fraction)

        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            sign = 1 if num >= 0 else -1
            num = abs(num)
            lcm = denominator * denom // gcd(denominator, denom)
            numerator = numerator * (lcm // denominator) + sign * num * (lcm // denom)
            denominator = lcm

        gcd_val = gcd(abs(numerator), denominator)
        numerator //= gcd_val
        denominator //= gcd_val

        return str(numerator) + '/' + str(denominator)