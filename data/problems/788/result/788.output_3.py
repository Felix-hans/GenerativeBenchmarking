# @lc app=leetcode id=788 lang=python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if self.isGoodNumber(i):
                count += 1
        return count

    def isGoodNumber(self, num: int) -> bool:
        valid_nums = {'2', '5', '6', '9'}
        invalid_nums = {'3', '4', '7'}
        num_str = str(num)
        has_valid_digit = False
        for digit in num_str:
            if digit in invalid_nums:
                return False
            if digit in valid_nums:
                has_valid_digit = True
        return has_valid_digit