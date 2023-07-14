# @lc app=leetcode id=2178 lang=python3
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = []
        largestEven = finalSum - (finalSum % 2)
        
        if largestEven == finalSum:
            result.append(largestEven)
            return result
        
        remainingSum = finalSum - largestEven
        start = 2
        
        while remainingSum > 0:
            if start % 2 == 0 and start <= remainingSum:
                result.append(start)
                remainingSum -= start
            start += 2
        
        if remainingSum == 0:
            return result
        else:
            return []