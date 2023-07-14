# @lc app=leetcode id=467 lang=python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        dp = [0] * 26  # Initialize the array to store the longest contiguous substring ending at each letter
        count = {}  # Dictionary to store the count of unique substrings ending at each letter
        length = len(s)
        max_length = 0  # Length of the longest contiguous substring
        
        for i in range(length):
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                max_length += 1
            else:
                max_length = 1
            
            index = ord(s[i]) - ord('a')
            dp[index] = max(dp[index], max_length)
        
        for length in dp:
            for j in range(length, 0, -1):
                index = (ord(s[j-1]) - ord('a'))
                count[index] = max(count.get(index, 0), j)
        
        return sum(count.values())