# @lc app=leetcode id=1358 lang=python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]  # count of 'a', 'b', 'c'
        num_substrings = 0
        left = 0

        for right in range(len(s)):
            counts[ord(s[right]) - ord('a')] += 1

            while all(counts):
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1

            num_substrings += left

        return num_substrings