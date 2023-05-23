# @lc app=leetcode id=166 lang=python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        
        if (numerator < 0) != (denominator < 0):
            result.append("-")

        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator // denominator))
        remainder = numerator % denominator

        if remainder != 0:
            result.append(".")
            decimal_part = []

            remainder_map = {}
            while remainder != 0:
                if remainder in remainder_map:
                    start = remainder_map[remainder]
                    decimal_part.insert(start, "(")
                    decimal_part.append(")")
                    break
                remainder_map[remainder] = len(decimal_part)

                remainder *= 10
                decimal_part.append(str(remainder // denominator))
                remainder %= denominator

            result.extend(decimal_part)
        
        return "".join(result)