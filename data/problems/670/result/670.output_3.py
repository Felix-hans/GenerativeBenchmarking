# @lc app=leetcode id=670 lang=python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        max_digit = -1
        max_index = -1

        for i, digit in enumerate(num_str):
            if int(digit) > max_digit:
                max_digit = int(digit)
                max_index = i

        if max_digit == -1:
            return num

        for i, digit in enumerate(num_str):
            if int(digit) < max_digit:
                num_str = num_str[:i] + num_str[max_index] + num_str[i+1:max_index] + digit + num_str[max_index+1:]
                break

        return int(num_str)