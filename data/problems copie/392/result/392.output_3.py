# @lc app=leetcode id=392 lang=python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_mapping = {}
        for i, char in enumerate(t):
            if char not in index_mapping:
                index_mapping[char] = []
            index_mapping[char].append(i)

        j = 0  # Pointer for string t

        for char in s:
            if char not in index_mapping:
                return False

            indices = index_mapping[char]
            left, right = 0, len(indices) - 1
            while left <= right:
                mid = (left + right) // 2
                if indices[mid] < j:
                    left = mid + 1
                else:
                    right = mid - 1

            if left == len(indices):
                return False

            j = indices[left] + 1

        return True