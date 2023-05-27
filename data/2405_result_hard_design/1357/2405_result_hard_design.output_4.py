# @lc app=leetcode id=2405_result_hard_design lang=python3
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
            product_id = product[i]
            product_amount = amount[i]
            product_index = self.products.index(product_id)
            subtotal += self.prices[product_index] * product_amount

        if self.customer_count % self.n == 0:
            subtotal = subtotal * ((100 - self.discount) / 100)

        return subtotal