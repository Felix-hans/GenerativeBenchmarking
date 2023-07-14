# @lc app=leetcode id=166 lang=python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = ""

        if (numerator < 0) ^ (denominator < 0):
            result += "-"

        numerator = abs(numerator)
        denominator = abs(denominator)

        quotient, remainder = divmod(numerator, denominator)

        result += str(quotient)

        if remainder == 0:
            return result

        result += "."

        remainders = {}

        while remainder != 0:
            if remainder in remainders:
                result = result[:remainders[remainder]] + "(" + result[remainders[remainder]:] + ")"
                break

            remainders[remainder] = len(result)

            quotient, remainder = divmod(remainder * 10, denominator)

            result += str(quotient)

        return result