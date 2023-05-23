# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        dp = [0] * (n + 1)  # dp[i] represents the number of distinct subsequences for s[:i]

        last_occurrence = [-1] * 26  # last_occurrence[c] stores the last index of character c

        dp[0] = 1  # Empty string has 1 distinct subsequence

        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod  # Double the count from the previous subsequence

            if last_occurrence[ord(s[i - 1]) - ord('a')] != -1:
                dp[i] -= dp[last_occurrence[ord(s[i - 1]) - ord('a')]]
            
            dp[i] %= mod  # Take modulo to avoid overflow

            last_occurrence[ord(s[i - 1]) - ord('a')] = i - 1

        return (dp[n] - 1) % mod  # Subtract 1 to exclude the empty string