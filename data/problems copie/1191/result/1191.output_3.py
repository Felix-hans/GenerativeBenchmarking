# @lc app=leetcode id=1191 lang=python3
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        max_subarray = self.maxSubarraySum(arr)
        total_sum = sum(arr)
        
        if total_sum < 0 and k <= 2:
            return max_subarray % (10**9 + 7)
        
        if k > 2:
            return max(max_subarray, (max_subarray + (k - 2) * total_sum) % (10**9 + 7))
        
        return max(max_subarray, (max_subarray + total_sum) % (10**9 + 7))
    
    def maxSubarraySum(self, arr: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = 0
        
        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum