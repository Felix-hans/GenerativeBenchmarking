# @lc app=leetcode id=1518 lang=python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles  # Total bottles consumed
        emptyBottles = numBottles  # Empty bottles left

        while emptyBottles >= numExchange:
            exchangedBottles = emptyBottles // numExchange
            totalBottles += exchangedBottles
            emptyBottles = exchangedBottles + (emptyBottles % numExchange)

        return totalBottles