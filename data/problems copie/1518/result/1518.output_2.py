# @lc app=leetcode id=1518 lang=python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drinks = numBottles  # Total number of bottles you can drink
        empty_bottles = numBottles  # Number of empty bottles you have after drinking
        while empty_bottles >= numExchange:
            full_bottles = empty_bottles // numExchange
            total_drinks += full_bottles
            empty_bottles = empty_bottles % numExchange + full_bottles
        return total_drinks