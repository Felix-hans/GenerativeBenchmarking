# @lc app=leetcode id=1103 lang=python3
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give_candies = 1
        idx = 0
        
        while candies > 0:
            result[idx] += min(give_candies, candies)
            candies -= give_candies
            give_candies += 1
            idx = (idx + 1) % num_people
        
        return result