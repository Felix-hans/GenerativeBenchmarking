# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                        "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                        "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                        "Seventeen", "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return "Zero"

        def helper(num):
            if num == 0:
                return ""

            if num < 20:
                return less_than_20[num] + " "

            if num < 100:
                return tens[num // 10] + " " + helper(num % 10)

            if num < 1000:
                return less_than_20[num // 100] + " Hundred " + helper(num % 100)

            for i, word in enumerate(thousands):
                if num < 1000 ** (i + 1):
                    return helper(num // 1000 ** i) + " " + word + " " + helper(num % 1000 ** i)

        return helper(num).strip()