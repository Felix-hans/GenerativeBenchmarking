# @lc app=leetcode id=1425 lang=python3
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            max_prev = max(dp[max(0, i-k):i])
            dp[i] = max(nums[i], nums[i] + max_prev)
            max_sum = max(max_sum, dp[i])

        return max_sum