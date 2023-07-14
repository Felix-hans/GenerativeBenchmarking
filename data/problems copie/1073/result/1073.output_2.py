# @lc app=leetcode id=1073 lang=python3
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        carry = 0
        i = len(arr1) - 1
        j = len(arr2) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += arr1[i]
                i -= 1
            if j >= 0:
                carry += arr2[j]
                j -= 1

            result.append(carry & 1)  # Get the current bit
            carry = -(carry >> 1)     # Update the carry value

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        result.reverse()
        return result