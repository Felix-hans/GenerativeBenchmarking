# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # Base case: No stones remaining, score is 0

        def calculateScore(index):
            if index >= n:
                return 0  # No more stones remaining, score is 0

            if dp[index] != float('-inf'):
                return dp[index]  # Return the precalculated score if available

            bestScore = float('-inf')
            currentSum = 0

            for i in range(index, min(index + 3, n)):
                currentSum += stoneValue[i]
                bestScore = max(bestScore, currentSum - calculateScore(i + 1))

            dp[index] = bestScore
            return bestScore

        aliceScore = calculateScore(0)
        bobScore = sum(stoneValue) - aliceScore

        if aliceScore > bobScore:
            return "Alice"
        elif aliceScore < bobScore:
            return "Bob"
        else:
            return "Tie"