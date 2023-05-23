# @lc app=leetcode id=1191 lang=python3
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(arr):
            max_sum = 0
            curr_sum = 0
            for num in arr:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum

        arr_sum = sum(arr)
        max_subarray_sum_original = kadane(arr)

        if k <= 2:
            return max(max_subarray_sum_original, 0)

        prefix_sum = [0] * len(arr)
        suffix_sum = [0] * len(arr)
        prefix_sum[0] = arr[0]
        suffix_sum[-1] = arr[-1]

        for i in range(1, len(arr)):
            prefix_sum[i] = prefix_sum[i-1] + arr[i]
            suffix_sum[-i-1] = suffix_sum[-i] + arr[-i-1]

        max_subarray_sum_prefix = kadane(prefix_sum)
        max_subarray_sum_suffix = kadane(suffix_sum)

        total_sum = arr_sum * k
        max_subarray_sum = max(max_subarray_sum_prefix + max_subarray_sum_suffix, 0) % MOD

        return max(max_subarray_sum, max_subarray_sum_original, 0)