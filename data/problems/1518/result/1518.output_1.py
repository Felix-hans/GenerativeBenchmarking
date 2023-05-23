# @lc app=leetcode id=1518 lang=python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles  # Total number of bottles initially
        emptyBottles = numBottles  # Number of empty bottles initially

        while emptyBottles >= numExchange:
            fullBottles = emptyBottles // numExchange
            remainingBottles = emptyBottles % numExchange
            totalBottles += fullBottles
            emptyBottles = fullBottles + remainingBottles

        return totalBottles