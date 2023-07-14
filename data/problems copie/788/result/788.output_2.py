# @lc app=leetcode id=788 lang=python3
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGoodNumber(num):
            rotation_map = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
            num_str = str(num)
            rotated_num = ''

            for digit in num_str:
                if digit in rotation_map:
                    rotated_num += rotation_map[digit]
                else:
                    return False  # If any digit cannot be rotated, the number is not good

            return rotated_num != num_str  # Check if the rotated number is different from the original number

        count = 0

        for num in range(1, n + 1):
            if isGoodNumber(num):
                count += 1

        return count