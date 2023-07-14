# @lc app=leetcode id=1556 lang=python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        result = []
        
        for i in range(len(n_str)):
            if i > 0 and i % 3 == 0:
                result.append('.')
            result.append(n_str[-i - 1])
        
        return ''.join(result[::-1])