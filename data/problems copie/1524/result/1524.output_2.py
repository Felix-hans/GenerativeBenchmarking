# @lc app=leetcode id=1524 lang=python3
class Solution:
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        result = 0
        prefix_sum = 0
        
        for num in arr:
            prefix_sum += num
            
            if prefix_sum % 2 == 0:
                result += odd_count
                even_count += 1
            else:
                result += even_count
                odd_count += 1
            
            result %= MOD
        
        return result