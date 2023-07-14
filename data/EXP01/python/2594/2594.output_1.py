# @lc app=leetcode id=2594 lang=python3
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort()  # sort ranks in ascending order
        total_time = 0  # initialize total time to 0
        
        for rank in reversed(ranks):
            num_cars = rank * rank  # calculate number of cars the mechanic can repair
            
            if num_cars >= cars:
                total_time += cars * rank * rank  # repair the remaining cars
                break  # exit the loop
                
            total_time += num_cars * rank * rank  # repair num_cars cars
            cars -= num_cars  # decrease the number of cars remaining
        
        return total_time