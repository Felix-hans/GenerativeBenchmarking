# @lc app=leetcode id=592 lang=python3
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = expression.replace('+', ' +').replace('-', ' -').split()
        result = sum(map(Fraction, fractions), Fraction(0, 1))
        return str(result.numerator) + '/' + str(result.denominator)