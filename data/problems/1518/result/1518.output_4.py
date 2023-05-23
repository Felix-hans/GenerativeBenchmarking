# @lc app=leetcode id=1518 lang=python3
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles  # Total bottles initially
        empty_bottles = numBottles  # Empty bottles initially

        while empty_bottles >= numExchange:
            full_bottles = empty_bottles // numExchange
            
            total_bottles += full_bottles
            
            empty_bottles = empty_bottles % numExchange + full_bottles

        return total_bottles