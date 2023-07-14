# @lc app=leetcode id=1524 lang=python3
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0  # Cumulative sum
        odd_count = 0  # Number of subarrays with odd sum
        even_count = 0  # Number of subarrays with even sum

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        return (odd_count * even_count) % (10**9 + 7)