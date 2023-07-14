# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        numerator, denominator = 0, 1
        
        fractions = expression.split('+')
        for fraction in fractions:
            if '-' in fraction:
                parts = fraction.split('-')
                sign = -1
            else:
                parts = fraction.split('/')
                sign = 1
            
            curr_numerator = int(parts[0]) * sign
            curr_denominator = int(parts[1])
            
            numerator = numerator * curr_denominator + curr_numerator * denominator
            denominator *= curr_denominator
            
        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor
        
        return str(numerator) + '/' + str(denominator)