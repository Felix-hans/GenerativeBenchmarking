# @lc app=leetcode id=273 lang=python3
class Solution:
    def __init__(self):
        self.less_than_20 = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        self.tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.less_than_20[num]

        result = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = self.helper(num % 1000) + self.thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()

    def helper(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)