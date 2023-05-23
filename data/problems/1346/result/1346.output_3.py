# @lc app=leetcode id=1346 lang=python3
class Solution:
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            seen.add(num)
        return False