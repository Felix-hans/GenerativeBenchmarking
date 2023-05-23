# @lc app=leetcode id=166 lang=python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_negative = (numerator < 0) != (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer_part = numerator // denominator
        remainder = numerator % denominator
        
        if remainder == 0:
            return str(integer_part) if not is_negative else "-" + str(integer_part)
        
        fractional_part = []
        remainder_map = {}
        repeating_start = -1
        
        while remainder != 0:
            if remainder in remainder_map:
                repeating_start = remainder_map[remainder]
                break
            
            remainder_map[remainder] = len(fractional_part)
            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder = remainder % denominator
        
        result = str(integer_part) + "." + "".join(fractional_part)
        
        if repeating_start != -1:
            result = result[:repeating_start + len(str(integer_part)) + 1] + "(" + result[repeating_start + len(str(integer_part)) + 1:] + ")"
        
        return result if not is_negative else "-" + result