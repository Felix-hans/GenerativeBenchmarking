# @lc app=leetcode id=1073 lang=python3
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        carry = 0
        i = len(arr1) - 1
        j = len(arr2) - 1

        while i >= 0 or j >= 0 or carry != 0:
            if i >= 0:
                carry += arr1[i]
                i -= 1
            if j >= 0:
                carry += arr2[j]
                j -= 1

            result.append(carry & 1)  # Adding the least significant bit to the result.
            carry = -(carry >> 1)  # Shifting the carry to the right and negating it.

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()  # Reversing the result to get the correct order.
        return result