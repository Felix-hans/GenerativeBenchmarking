# @lc app=leetcode id=1103 lang=python3
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        current_candies = 1
        idx = 0
        
        while candies > 0:
            result[idx % num_people] += min(candies, current_candies)
            candies -= current_candies
            current_candies += 1
            idx += 1
        
        return result