# @lc app=leetcode id=1073 lang=python3
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.reverse()
        arr2.reverse()

        result = []
        carry = 0
        i = 0

        while i < len(arr1) or i < len(arr2) or carry != 0:
            digit1 = arr1[i] if i < len(arr1) else 0
            digit2 = arr2[i] if i < len(arr2) else 0

            current_sum = digit1 + digit2 + carry

            remainder = current_sum % 2
            carry = -(current_sum // 2)  # Integer division to handle negative carry

            result.append(remainder)

            i += 1

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()

        return result