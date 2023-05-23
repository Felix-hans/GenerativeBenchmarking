# @lc app=leetcode id=1239 lang=python3
class Solution:
    def maxLength(self, arr):
        self.max_len = 0  # variable to store the maximum length
        
        def backtrack(curr, idx):
            if len(set(curr)) != len(curr):  # check if current subsequence has duplicate characters
                return
            
            self.max_len = max(self.max_len, len(curr))  # update maximum length
            
            for i in range(idx, len(arr)):
                backtrack(curr + arr[i], i + 1)  # recursive call to generate all possible subsequences
        
        backtrack("", 0)  # start with an empty subsequence at index 0
        return self.max_len