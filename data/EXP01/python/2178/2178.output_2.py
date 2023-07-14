# @lc app=leetcode id=2178 lang=python3
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = []
        currentSum = 0
        
        for num in range(2, finalSum + 1, 2):
            if num <= finalSum - currentSum:
                result.append(num)
                currentSum += num
        
        if currentSum == finalSum:
            return result
        else:
            return []