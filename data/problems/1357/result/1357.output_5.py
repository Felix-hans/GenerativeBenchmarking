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
        subtotal = 0.0
        for i in range(len(product)):
            prod_id = product[i]
            prod_amount = amount[i]
            prod_index = self.products.index(prod_id)
            prod_price = self.prices[prod_index]
            subtotal += prod_amount * prod_price
        
        if self.customer_count % self.n == 0:
            subtotal -= (subtotal * self.discount) / 100
        
        return subtotal