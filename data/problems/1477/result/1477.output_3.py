# @lc app=leetcode id=1477 lang=python3
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sums = self.calculatePrefixSums(arr, target)
        suffix_sums = self.calculateSuffixSums(arr, target)
        n = len(arr)

        min_sum_lengths = float('inf')
        for i in range(n):
            if prefix_sums[i] != float('inf') and suffix_sums[i+1] != float('inf'):
                min_sum_lengths = min(min_sum_lengths, prefix_sums[i] + suffix_sums[i+1])

        return min_sum_lengths if min_sum_lengths != float('inf') else -1

    def calculatePrefixSums(self, arr: List[int], target: int) -> List[int]:
        n = len(arr)
        prefix_sums = [float('inf')] * (n + 1)
        prefix_sum = 0
        start = 0

        for end in range(n):
            prefix_sum += arr[end]
            while prefix_sum > target:
                prefix_sum -= arr[start]
                start += 1
            if prefix_sum == target:
                prefix_sums[end+1] = min(prefix_sums[end], end - start + 1)
            else:
                prefix_sums[end+1] = prefix_sums[end]

        return prefix_sums

    def calculateSuffixSums(self, arr: List[int], target: int) -> List[int]:
        n = len(arr)
        suffix_sums = [float('inf')] * (n + 1)
        suffix_sum = 0
        end = n - 1

        for start in range(n - 1, -1, -1):
            suffix_sum += arr[start]
            while suffix_sum > target:
                suffix_sum -= arr[end]
                end -= 1
            if suffix_sum == target:
                suffix_sums[start] = min(suffix_sums[start+1], end - start + 1)
            else:
                suffix_sums[start] = suffix_sums[start+1]

        return suffix_sums