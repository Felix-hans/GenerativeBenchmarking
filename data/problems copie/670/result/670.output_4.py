# @lc app=leetcode id=670 lang=python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))

        for i in range(len(digits)):
            max_digit = digits[i]
            max_index = i

            for j in range(i + 1, len(digits)):
                if digits[j] >= max_digit:
                    max_digit = digits[j]
                    max_index = j

            if max_digit > digits[i]:
                digits[i], digits[max_index] = digits[max_index], digits[i]
                return int(''.join(digits))

        return num