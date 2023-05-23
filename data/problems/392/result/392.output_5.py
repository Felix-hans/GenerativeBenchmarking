# @lc app=leetcode id=392 lang=python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_indices = {}

        for i, char in enumerate(t):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)

        subsequence_length = len(s)
        main_length = len(t)

        main_index = 0

        for char in s:
            if char not in char_indices:
                return False

            indices = char_indices[char]

            left = 0
            right = len(indices) - 1
            while left <= right:
                mid = (left + right) // 2
                if indices[mid] <= main_index:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(indices):
                return False

            main_index = indices[left] + 1

        return True