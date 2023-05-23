# @lc app=leetcode id=1122 lang=python3
class Solution:
    def relativeSortArray(self, arr1, arr2):
        relative_order = {num: index for index, num in enumerate(arr2)}
        included = []
        excluded = []

        for num in arr1:
            if num in relative_order:
                included.append(num)
            else:
                excluded.append(num)

        excluded.sort()

        included.sort(key=lambda x: relative_order[x])

        return included + excluded