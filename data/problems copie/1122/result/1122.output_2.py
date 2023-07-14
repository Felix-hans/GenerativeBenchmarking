# @lc app=leetcode id=1122 lang=python3
class Solution:
    def relativeSortArray(self, arr1, arr2):
        counts = {}
        for num in arr1:
            counts[num] = counts.get(num, 0) + 1
        
        sorted_arr = []
        for num in arr2:
            sorted_arr.extend([num] * counts[num])
            del counts[num]
        
        for num in sorted(counts.keys()):
            sorted_arr.extend([num] * counts[num])
        
        return sorted_arr