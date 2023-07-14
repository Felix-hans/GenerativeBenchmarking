# @lc app=leetcode id=1103 lang=python3
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        distribution = [0] * num_people  # Initialize the distribution array
        give_candies = 1  # Number of candies to give in each turn
        index = 0  # Index of the person to receive the candies

        while candies > 0:
            distribution[index] += min(candies, give_candies)
            candies -= give_candies

            index = (index + 1) % num_people
            give_candies += 1

        return distribution