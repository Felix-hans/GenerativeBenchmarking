# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for val, index in queries:
            nums[index] += val

            if nums[index] % 2 == 0:
                even_sum += nums[index]
            elif nums[index] - val % 2 == 0:
                even_sum -= nums[index] - val

            result.append(even_sum)

        return result