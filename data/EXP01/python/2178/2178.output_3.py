# @lc app=leetcode id=2178 lang=python3
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        result = []
        remainingSum = finalSum

        for i in range(2, finalSum + 1, 2):
            if remainingSum >= i:
                result.append(i)
                remainingSum -= i
            else:
                break

        if remainingSum == 0:
            return result
        else:
            return []