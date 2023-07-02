# @lc app=leetcode id=1092 lang=python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        supersequence = ''
        i, j = m, n
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                supersequence = str1[i - 1] + supersequence
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                supersequence = str1[i - 1] + supersequence
                i -= 1
            else:
                supersequence = str2[j - 1] + supersequence
                j -= 1
        
        while i > 0:
            supersequence = str1[i - 1] + supersequence
            i -= 1
        while j > 0:
            supersequence = str2[j - 1] + supersequence
            j -= 1
        
        return supersequence