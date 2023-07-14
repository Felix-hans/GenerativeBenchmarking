# @lc app=leetcode id=1524 lang=python3
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = int(1e9) + 7
        prefix_sum = [0] * len(arr)
        prefix_sum[0] = arr[0]
        count = 0
        odd_count = 0
        
        for i in range(1, len(arr)):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]
        
        for sum in prefix_sum:
            if sum % 2 == 0:
                count += odd_count
            else:
                count += 1
                odd_count += 1
        
        return count % mod