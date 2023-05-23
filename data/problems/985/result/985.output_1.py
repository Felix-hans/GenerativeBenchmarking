# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for query in queries:
            val, index = query[0], query[1]
            old_val = nums[index]
            nums[index] += val
            new_val = nums[index]

            if old_val % 2 == 0:
                even_sum -= old_val

            if new_val % 2 == 0:
                even_sum += new_val

            result.append(even_sum)

        return result