# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        even_sum = sum(num for num in nums if num % 2 == 0)

        answer = []

        for val, index in queries:
            is_even = nums[index] % 2 == 0

            nums[index] += val

            is_updated_even = nums[index] % 2 == 0

            if is_even:
                even_sum -= nums[index] - val
            if is_updated_even:
                even_sum += nums[index]

            answer.append(even_sum)

        return answer