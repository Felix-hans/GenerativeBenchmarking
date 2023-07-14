# @lc app=leetcode id=2135 lang=python
class Solution:
    def wordCount(self, startWords, targetWords):
        count = 0   # to keep track of the number of strings that can be formed
        
        for target in targetWords:
            for start in startWords:
                start_set = set(start)
                target_set = set(target)
                
                if target_set.issubset(start_set):
                    count += 1   # increment count if it is possible to obtain target from start
                    break
                    
        return count