# @lc app=leetcode id=1458 lang=python3
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1],  # Include current elements
                    dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],  # Extend previous subsequences
                    dp[i - 1][j],  # Exclude current element from nums2
                    dp[i][j - 1]  # Exclude current element from nums1
                )
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])  # Check if previous subsequence is the maximum

        return dp[m][n]