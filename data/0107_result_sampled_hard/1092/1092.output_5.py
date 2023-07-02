# @lc app=leetcode id=1092 lang=python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [""] * (n + 1)
        
        for j in range(n + 1):
            dp[j] = str2[:j]
        
        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = str1[:i]
            for j in range(1, n + 1):
                curr = dp[j]
                if str1[i - 1] == str2[j - 1]:
                    dp[j] = prev + str1[i - 1]
                else:
                    if len(dp[j - 1]) < len(dp[j]):
                        dp[j] = dp[j - 1] + str2[j - 1]
                    else:
                        dp[j] = dp[j] + str1[i - 1]
                prev = curr
        
        return dp[n]