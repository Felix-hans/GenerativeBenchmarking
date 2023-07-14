# @lc app=leetcode id=2442 lang=python3
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_integers = set(nums)
        
        for num in nums:
            reversed_num = int(str(num)[::-1])
            distinct_integers.add(reversed_num)
        
        return len(distinct_integers)