# @lc app=leetcode id=592 lang=python3
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = self.parse_fractions(expression)
        result = self.calculate_sum(fractions)
        return self.format_fraction(result)
    
    def parse_fractions(self, expression: str):
        fractions = []
        start = 0
        for i in range(1, len(expression)):
            if expression[i] in ['+', '-']:
                fractions.append(expression[start:i])
                start = i
        fractions.append(expression[start:])
        return fractions
    
    def calculate_sum(self, fractions):
        numerator = 0
        denominator = 1
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            numerator = numerator * denom + num * denominator
            denominator *= denom
        return (numerator, denominator)
    
    def format_fraction(self, fraction):
        numerator, denominator = fraction
        if numerator == 0:
            return '0/1'
        gcd = self.gcd(abs(numerator), denominator)
        numerator //= gcd
        denominator //= gcd
        if denominator == 1:
            return str(numerator) + '/1'
        else:
            return str(numerator) + '/' + str(denominator)
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a