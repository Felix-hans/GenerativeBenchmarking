# @lc app=leetcode id=392 lang=python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = {}  # Dictionary to store positions of characters in t

        for i, char in enumerate(t):
            if char not in index:
                index[char] = []
            index[char].append(i)

        prev_pos = -1  # Previous position of character in t

        for char in s:
            if char not in index:
                return False  # Character does not exist in t

            positions = index[char]
            found = False

            left, right = 0, len(positions) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if positions[mid] > prev_pos:
                    found = True
                    prev_pos = positions[mid]
                    break
                elif positions[mid] < prev_pos:
                    left = mid + 1
                else:
                    right = mid - 1

            if not found:
                return False  # Character not found in the correct order

        return True  # All characters in s found in the correct order in t