# @lc app=leetcode id=1092 lang=python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        for i in range(len(str1) + 1):
            dp[i][0] = i
        for j in range(len(str2) + 1):
            dp[0][j] = j

        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

        supersequence = ""
        i, j = len(str1), len(str2)
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                supersequence = str1[i - 1] + supersequence
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
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