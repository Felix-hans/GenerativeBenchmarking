# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        multiples_of_ten = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(num):
            if num == 0:
                return ""
            elif num < 10:
                return singles[num] + " "
            elif num < 20:
                return tens[num - 10] + " "
            elif num < 100:
                return multiples_of_ten[num // 10] + " " + helper(num % 10)
            else:
                return singles[num // 100] + " Hundred " + helper(num % 100)
        
        words = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                words = helper(num % 1000) + thousands[i] + " " + words
            num //= 1000
            i += 1
        
        return words.strip()