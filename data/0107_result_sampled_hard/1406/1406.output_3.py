# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        memo = [None] * n

        def calculateScore(index):
            if index >= n:
                return 0

            if memo[index] is not None:
                return memo[index]

            bestScore = float('-inf')
            totalStones = 0

            for i in range(index, min(index + 3, n)):
                totalStones += stoneValue[i]
                bestScore = max(bestScore, totalStones - calculateScore(i + 1))

            memo[index] = bestScore
            return bestScore

        aliceScore = calculateScore(0)
        bobScore = sum(stoneValue) - aliceScore

        if aliceScore > bobScore:
            return "Alice"
        elif aliceScore < bobScore:
            return "Bob"
        else:
            return "Tie"