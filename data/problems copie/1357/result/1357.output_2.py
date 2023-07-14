# @lc app=leetcode id=1357 lang=python3
from typing import List

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        subtotal = 0

        for i in range(len(product)):
            index = self.products.index(product[i])  # Find the index of the product
            subtotal += self.prices[index] * amount[i]  # Calculate the subtotal

        if self.customer_count % self.n == 0:  # Apply discount if it's the nth customer
            subtotal = subtotal * ((100 - self.discount) / 100)

        return subtotal