# @lc app=leetcode id=1556 lang=python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        
        num_digits = len(n_str)
        
        if num_digits <= 3:
            return n_str
        
        num_separators = (num_digits - 1) // 3
        
        result = n_str[:num_digits % 3] if num_digits % 3 != 0 else ''
        
        for i in range(num_separators):
            start = num_digits % 3 + i * 3
            end = start + 3
            result += '.' + n_str[start:end]
        
        return result