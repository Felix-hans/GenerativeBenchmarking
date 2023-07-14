# @lc app=leetcode id=1358 lang=python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counts = [0, 0, 0]  # Frequency counts of 'a', 'b', 'c'
        left = 0  # Left pointer of the sliding window
        substr_count = 0  # Number of substrings containing 'a', 'b', and 'c'

        for right in range(len(s)):
            counts[ord(s[right]) - ord('a')] += 1  # Update the character count

            while all(counts):
                counts[ord(s[left]) - ord('a')] -= 1
                left += 1

            substr_count += left

        return substr_count