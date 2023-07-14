# @lc app=leetcode id=788 lang=python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n+1):
            if self.isGoodNumber(num):
                count += 1
        return count

    def isGoodNumber(self, num: int) -> bool:
        rotated = ""
        for digit in str(num):
            if digit in "018":
                rotated += digit
            elif digit == "2":
                rotated += "5"
            elif digit == "5":
                rotated += "2"
            elif digit == "6":
                rotated += "9"
            elif digit == "9":
                rotated += "6"
            else:
                return False
        return rotated != str(num)