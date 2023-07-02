# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            ones = [
                "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"
            ]
            return ones[num]

        def two_less_20(num):
            if num < 20:
                return one(num)
            tens = [
                "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
            ]
            return tens[num // 10] + " " + one(num % 10)

        def three(num):
            hundred = num // 100
            rest = num % 100
            if hundred and rest:
                return one(hundred) + " Hundred " + two_less_20(rest)
            elif hundred:
                return one(hundred) + " Hundred"
            else:
                return two_less_20(rest)

        groups = [
            "", "Thousand", "Million", "Billion"
        ]

        words = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                words = three(num % 1000) + " " + groups[i] + " " + words
            num //= 1000
            i += 1

        return words.strip()