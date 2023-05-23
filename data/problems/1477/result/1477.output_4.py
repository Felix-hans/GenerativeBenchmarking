# @lc app=leetcode id=1477 lang=python3
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = [0] * (n + 1)  # Prefix sum array
        left_window = [float('inf')] * (n + 1)  # Minimum length of subarray with target sum ending at each index from the left
        right_window = [float('inf')] * (n + 2)  # Minimum length of subarray with target sum starting at each index from the right

        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

        left_start = 0
        for right_end in range(1, n + 1):
            while prefix_sum[right_end] - prefix_sum[left_start] > target:
                left_start += 1
            if prefix_sum[right_end] - prefix_sum[left_start] == target:
                left_window[right_end] = right_end - left_start

        right_end = n
        for left_start in range(n, 0, -1):
            while prefix_sum[right_end] - prefix_sum[left_start - 1] > target:
                right_end -= 1
            if prefix_sum[right_end] - prefix_sum[left_start - 1] == target:
                right_window[left_start] = right_end - left_start + 1

        min_length_sum = float('inf')
        for i in range(1, n + 1):
            min_length_sum = min(min_length_sum, left_window[i - 1] + right_window[i + 1])

        return min_length_sum if min_length_sum != float('inf') else -1