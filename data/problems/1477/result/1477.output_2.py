# @lc app=leetcode id=1477 lang=python3
from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sums = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sums[i+1] = prefix_sums[i] + arr[i]
        
        left_lengths = [float('inf')] * len(arr)  # minimum length of sub-array ending at index i with sum = target
        right_lengths = [float('inf')] * len(arr)  # minimum length of sub-array starting at index i with sum = target
        
        left = 0
        window_sum = 0
        for right in range(len(arr)):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
            
            if window_sum == target:
                length = right - left + 1
                if left > 0:
                    left_lengths[right] = min(left_lengths[right-1], length)
                else:
                    left_lengths[right] = length
        
        left = len(arr) - 1
        window_sum = 0
        
        for right in range(len(arr)-1, -1, -1):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                left -= 1
            
            if window_sum == target:
                length = left - right + 1
                if right < len(arr) - 1:
                    right_lengths[right] = min(right_lengths[right+1], length)
                else:
                    right_lengths[right] = length
        
        min_length_sum = float('inf')
        
        for i in range(len(arr) - 1):
            if left_lengths[i] != float('inf') and right_lengths[i+1] != float('inf'):
                min_length_sum = min(min_length_sum, left_lengths[i] + right_lengths[i+1])
        
        if min_length_sum == float('inf'):
            return -1
        else:
            return min_length_sum