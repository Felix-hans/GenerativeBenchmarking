# @lc app=leetcode id=1092 lang=python3
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        
        i, j = m, n
        superseq = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                superseq.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                superseq.append(str1[i - 1])
                i -= 1
            else:
                superseq.append(str2[j - 1])
                j -= 1
        
        while i > 0:
            superseq.append(str1[i - 1])
            i -= 1
        while j > 0:
            superseq.append(str2[j - 1])
            j -= 1
        
        superseq.reverse()
        return ''.join(superseq)