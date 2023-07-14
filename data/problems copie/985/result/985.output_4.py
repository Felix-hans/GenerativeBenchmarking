# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        even_sum = sum(num for num in nums if num % 2 == 0)

        for val, index in queries:
            if nums[index] % 2 == 0:
                even_sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                even_sum += nums[index]
            answer.append(even_sum)

        return answer