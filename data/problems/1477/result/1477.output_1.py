# @lc app=leetcode id=1477 lang=python3
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sums = self.calculatePrefixSums(arr)
        subarray_sums = {}  # Stores the minimum subarray length for each sum

        left_subarray_length = float('inf')
        result = float('inf')

        current_sum = 0
        for right, num in enumerate(arr):
            current_sum += num

            if current_sum - target in subarray_sums:
                left = subarray_sums[current_sum - target]
                left_subarray_length = min(left_subarray_length, right - left + 1)

            if current_sum in subarray_sums:
                subarray_sums[current_sum] = min(subarray_sums[current_sum], right)
            else:
                subarray_sums[current_sum] = right

            if current_sum - target in prefix_sums:
                result = min(result, prefix_sums[current_sum - target] + left_subarray_length)

        return result if result != float('inf') else -1

    def calculatePrefixSums(self, arr: List[int]) -> dict:
        prefix_sums = {}
        current_sum = 0
        for i, num in enumerate(arr):
            current_sum += num
            if current_sum not in prefix_sums:
                prefix_sums[current_sum] = i + 1  # Store the prefix sum up to index i
        return prefix_sums