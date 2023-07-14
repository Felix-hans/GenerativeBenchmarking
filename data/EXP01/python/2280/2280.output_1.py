# @lc app=leetcode id=2280 lang=python3
class Solution:
    def minimumLines(self, stockPrices):
        count = 1  # start with one line
        prev_price = stockPrices[0][1]  # initialize the previous price

        for i in range(1, len(stockPrices)):
            curr_price = stockPrices[i][1]  # get the current price

            if curr_price != prev_price:
                count += 1  # increment the count of lines
                prev_price = curr_price  # update the previous price

        return count