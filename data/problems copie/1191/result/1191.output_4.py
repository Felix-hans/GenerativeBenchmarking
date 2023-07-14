# @lc app=leetcode id=1191 lang=python3
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        max_sum = 0
        current_sum = 0
        
        for i in range(n):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        prefix_sum[0] = arr[0]
        suffix_sum[n-1] = arr[n-1]
        
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]
            suffix_sum[n-1-i] = suffix_sum[n-i] + arr[n-1-i]
        
        total_sum = sum(arr)
        
        if total_sum > 0:
            max_prefix_suffix_sum = max(prefix_sum) + max(suffix_sum) + (k-2) * total_sum
        else:
            max_prefix_suffix_sum = 0
        
        max_combined_sum = max(suffix_sum) + max(prefix_sum)
        
        result = max(max_sum, max_prefix_suffix_sum, max_combined_sum)
        
        return result % (10**9 + 7)