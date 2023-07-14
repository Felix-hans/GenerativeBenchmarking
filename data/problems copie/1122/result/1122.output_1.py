# @lc app=leetcode id=1122 lang=python3
class Solution:
    def relativeSortArray(self, arr1, arr2):
        def custom_sort(x):
            if x in arr2:
                return (arr2.index(x), x)
            else:
                return (len(arr2), x)

        return sorted(arr1, key=custom_sort)