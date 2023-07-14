# @lc app=leetcode id=1518 lang=python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles  # Initialize the total number of bottles
        emptyBottles = numBottles  # Initialize the number of empty bottles

        while emptyBottles >= numExchange:
            newBottles = emptyBottles // numExchange
            totalBottles += newBottles
            emptyBottles = newBottles + emptyBottles % numExchange

        return totalBottles