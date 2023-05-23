# @lc app=leetcode id=273 lang=python3
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        singles = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']
        
        def helper(n):
            if n == 0:
                return ''
            elif n < 10:
                return singles[n] + ' '
            elif n < 20:
                return teens[n - 10] + ' '
            elif n < 100:
                return tens[n // 10] + ' ' + helper(n % 10)
            else:
                return singles[n // 100] + ' Hundred ' + helper(n % 100)
        
        words = ''
        i = 0
        
        while num > 0:
            if num % 1000 != 0:
                words = helper(num % 1000) + thousands[i] + ' ' + words
            num //= 1000
            i += 1
        
        return words.strip()