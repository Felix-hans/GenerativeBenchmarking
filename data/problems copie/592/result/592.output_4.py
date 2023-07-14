# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        i = 0
        while i < len(expression):
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1

            num = 0
            while i < len(expression) and expression[i] != '/':
                num = num * 10 + int(expression[i])
                i += 1

            i += 1

            den = 0
            while i < len(expression) and expression[i] not in ['+', '-']:
                den = den * 10 + int(expression[i])
                i += 1

            num *= sign
            numerator = numerator * den + num * denominator
            denominator *= den

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        return str(numerator) + '/' + str(denominator)