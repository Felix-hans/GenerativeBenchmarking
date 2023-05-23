# @lc app=leetcode id=1346 lang=python3
class Solution:
    def checkIfExist(self, arr):
        num_count = {}
        for num in arr:
            if num * 2 in num_count or num / 2 in num_count:
                return True
            num_count[num] = True
        return False