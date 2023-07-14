# @lc app=leetcode id=1556 lang=python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        num_str = str(n)

        if len(num_str) < 4:
            return num_str

        result = ""

        for i in range(len(num_str) - 1, -1, -1):
            result = num_str[i] + result

            if i > 0 and (len(num_str) - i) % 3 == 0:
                result = "." + result

        return result