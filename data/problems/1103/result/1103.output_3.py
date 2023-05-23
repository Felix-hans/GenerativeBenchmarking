# @lc app=leetcode id=1103 lang=python3
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 0  # Index of the current person
        
        while candies > 0:
            candies_to_give = min(candies, i + 1)
            
            result[i] += candies_to_give
            
            candies -= candies_to_give
            i = (i + 1) % num_people
        
        return result