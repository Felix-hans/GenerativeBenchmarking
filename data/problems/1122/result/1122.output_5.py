# @lc app=leetcode id=1122 lang=python3
class Solution:
    def relativeSortArray(self, arr1, arr2):
        indices = {num: i for i, num in enumerate(arr2)}

        def custom_sort_key(num):
            if num in indices:
                return indices[num]
            else:
                return len(arr2) + num

        arr1.sort(key=custom_sort_key)
        return arr1