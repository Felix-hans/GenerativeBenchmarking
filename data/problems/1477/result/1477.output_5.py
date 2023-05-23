# @lc app=leetcode id=1477 lang=python3
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        left_sum = [float('inf')] * n  # Minimum subarray length with sum equal to target from the left side
        right_sum = [float('inf')] * n  # Minimum subarray length with sum equal to target from the right side
        prefix_sum = {0: -1}  # Prefix sum dictionary (sum: index)
        curr_sum = 0  # Current sum
        min_length = float('inf')  # Minimum sum of subarray lengths

        for i in range(n):
            curr_sum += arr[i]
            if curr_sum - target in prefix_sum:
                left_length = i - prefix_sum[curr_sum - target]
                left_sum[i] = min(left_length, left_sum[i - 1])
            else:
                left_sum[i] = left_sum[i - 1]
            prefix_sum[curr_sum] = i

        prefix_sum = {0: n}  # Prefix sum dictionary (sum: index)
        curr_sum = 0  # Current sum

        for i in range(n - 1, -1, -1):
            curr_sum += arr[i]
            if curr_sum - target in prefix_sum:
                right_length = prefix_sum[curr_sum - target] - i
                right_sum[i] = min(right_length, right_sum[i + 1])
            else:
                right_sum[i] = right_sum[i + 1]
            prefix_sum[curr_sum] = i

        for i in range(n - 1):
            min_length = min(min_length, left_sum[i] + right_sum[i + 1])

        if min_length == float('inf'):
            return -1
        else:
            return min_length