# @lc app=leetcode id=166 lang=python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) ^ (denominator < 0) else ""

        numerator = abs(numerator)
        denominator = abs(denominator)

        integer_part = numerator // denominator
        remainder = numerator % denominator

        if remainder == 0:
            return sign + str(integer_part)

        fractional_part = []
        remainders = {}

        while remainder != 0:
            if remainder in remainders:
                index = remainders[remainder]
                fractional_part.insert(index, "(")
                fractional_part.append(")")
                break

            remainders[remainder] = len(fractional_part)

            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder %= denominator

        result = sign + str(integer_part) + "." + "".join(fractional_part)
        return result