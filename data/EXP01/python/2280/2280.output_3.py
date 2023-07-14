# @lc app=leetcode id=2280 lang=python3
class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        line_count = 1
        prev_price = stockPrices[0][1]
        for i in range(1, len(stockPrices)):
            if stockPrices[i][1] != prev_price:
                line_count += 1
            prev_price = stockPrices[i][1]
        return line_count