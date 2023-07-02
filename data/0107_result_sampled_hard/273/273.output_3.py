# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
            "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
            "Eighty", "Ninety"
        ]

        magnitudes = ["", "Thousand", "Million", "Billion"]

        def convert_chunk(num):
            if num == 0:
                return ""
            elif num < 20:
                return less_than_20[num] + " "
            elif num < 100:
                return tens[num // 10] + " " + convert_chunk(num % 10)
            else:
                return less_than_20[num // 100] + " Hundred " + convert_chunk(num % 100)

        words = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                words = convert_chunk(num % 1000) + magnitudes[i] + " " + words
            num //= 1000
            i += 1

        return words.strip()