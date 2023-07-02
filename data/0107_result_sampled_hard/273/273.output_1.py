# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one_to_word(num):
            ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            return ones[num]

        def two_less_20_to_word(num):
            less_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                       "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                       "Eighteen", "Nineteen"]
            return less_20[num]

        def ten_to_word(num):
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            return tens[num]

        def two_to_word(num):
            if not num:
                return ""
            elif num < 20:
                return two_less_20_to_word(num)
            else:
                ten = num // 10
                rest = num % 10
                return ten_to_word(ten) + " " + one_to_word(rest) if rest else ten_to_word(ten)

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        result = ""
        if billion:
            result += self.numberToWords(billion) + " Billion "
        if million:
            result += self.numberToWords(million) + " Million "
        if thousand:
            result += self.numberToWords(thousand) + " Thousand "
        if rest:
            result += self.numberToWords(rest)

        return result.strip()