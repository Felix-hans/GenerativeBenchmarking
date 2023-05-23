# @lc app=leetcode id=1191 lang=python3
class Solution:
    def max_subarray_sum(self, nums):
        max_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

    def kConcatenationMaxSum(self, arr, k):
        if k <= 1:
            return self.max_subarray_sum(arr) % (10**9 + 7)

        total_sum = sum(arr)
        if total_sum <= 0:
            return 0

        max_sum = self.max_subarray_sum(arr)
        prefix = [0] * len(arr)
        suffix = [0] * len(arr)
        prefix[0] = arr[0]
        suffix[-1] = arr[-1]
        for i in range(1, len(arr)):
            prefix[i] = max(arr[i], prefix[i-1] + arr[i])
            suffix[-i-1] = max(arr[-i-1], suffix[-i] + arr[-i-1])

        subarray_sum = prefix[-1] + suffix[0]
        if max_sum < 0:
            return subarray_sum % (10**9 + 7)
        else:
            return max(max_sum, subarray_sum + (k-2) * total_sum) % (10**9 + 7)