# @lc app=leetcode id=166 lang=python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '-' if numerator * denominator < 0 else ''
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        integer_part = numerator // denominator
        
        remainder = numerator % denominator
        
        if remainder == 0:
            return sign + str(integer_part)
        
        fractional_part = []
        
        remainders = {}
        
        while remainder != 0:
            if remainder in remainders:
                index = remainders[remainder]
                fractional_part.insert(index, '(')
                fractional_part.append(')')
                break
            
            remainders[remainder] = len(fractional_part)
            
            quotient, remainder = divmod(remainder * 10, denominator)
            fractional_part.append(str(quotient))
        
        decimal_str = sign + str(integer_part) + '.' + ''.join(fractional_part)
        
        return decimal_str