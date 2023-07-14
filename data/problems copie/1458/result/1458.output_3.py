# @lc app=leetcode id=1458 lang=python3
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [[float('-inf')] * (n2 + 1) for _ in range(n1 + 1)]
        
        dp[0][0] = 0
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                curr_product = nums1[i - 1] * nums2[j - 1]
                
                dp[i][j] = max(
                    curr_product,                    # Dot product of current elements only
                    dp[i - 1][j - 1] + curr_product,  # Extend the previous subsequences
                    dp[i - 1][j],                    # Ignore current element from nums2
                    dp[i][j - 1]                     # Ignore current element from nums1
                )
        
        return dp[n1][n2]