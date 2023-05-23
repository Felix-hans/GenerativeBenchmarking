# @lc app=leetcode id=1556 lang=python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n_str = str(n)
        length = len(n_str)
        result = []

        for i in range(length):
            if i > 0 and (length - i) % 3 == 0:
                result.append('.')
            result.append(n_str[i])

        return ''.join(result)