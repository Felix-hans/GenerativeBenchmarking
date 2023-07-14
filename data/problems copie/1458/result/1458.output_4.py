# @lc app=leetcode id=1458 lang=python3
class Solution:
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i-1][j-1] + nums1[i-1] * nums2[j-1], dp[i][j-1], dp[i-1][j])
        
        return dp[m][n]