# @lc app=leetcode id=767 lang=python3
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1

        sorted_chars = sorted(char_freq, key=lambda x: char_freq[x], reverse=True)

        if char_freq[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""

        rearranged = [''] * len(s)
        idx = 0

        for char in sorted_chars:
            while char_freq[char] > 0 and idx < len(s) and idx % 2 == 0:
                rearranged[idx] = char
                char_freq[char] -= 1
                idx += 1

        for char in sorted_chars:
            while char_freq[char] > 0 and idx < len(s) and idx % 2 != 0:
                rearranged[idx] = char
                char_freq[char] -= 1
                idx += 1

        return ''.join(rearranged)