# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                "Eighteen", "Nineteen"]

        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_group(num):
            if num == 0:
                return ""

            if num < 20:
                return ones[num] + " "

            if num < 100:
                return tens[num // 10] + " " + convert_group(num % 10)

            return ones[num // 100] + " Hundred " + convert_group(num % 100)

        words = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                words = convert_group(num % 1000) + thousands[i] + " " + words

            num //= 1000
            i += 1

        return words.strip()