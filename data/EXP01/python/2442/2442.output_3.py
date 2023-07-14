# @lc app=leetcode id=2442 lang=python3
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_integers = set()

        for num in nums:
            reverse_num = int(str(num)[::-1])
            distinct_integers.add(reverse_num)

        return len(distinct_integers)