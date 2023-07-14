# @lc app=leetcode id=1191 lang=python3
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7

        array_sum = sum(arr)

        if array_sum < 0:
            return 0

        if k == 1:
            return self.maxSubarraySum(arr) % mod

        max_subarray_sum = self.maxSubarraySum(arr + arr) % mod

        if array_sum > 0:
            return (max_subarray_sum + (k - 2) * array_sum) % mod

        return max_subarray_sum

    def maxSubarraySum(self, arr: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0

        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum