# @lc app=leetcode id=1358 lang=python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0  # Number of valid substrings
        freq = {char: 0 for char in 'abc'}  # Frequency count of 'a', 'b', and 'c'
        left = 0  # Left pointer of the sliding window

        for right in range(len(s)):
            freq[s[right]] += 1  # Increment the frequency count of the current character

            while all(freq.values()):
                count += len(s) - right  # Add the number of valid substrings ending at the current position
                freq[s[left]] -= 1  # Decrement the frequency count of the left character
                left += 1  # Move the left pointer to the right

        return count