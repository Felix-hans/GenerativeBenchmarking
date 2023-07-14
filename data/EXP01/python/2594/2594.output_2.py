# @lc app=leetcode id=2594 lang=python3
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        ranks.sort(reverse=True)  # Sort ranks array in descending order
        
        time_taken = 0
        for rank in ranks:
            num_cars = min(cars, rank)  # Assign as many cars as possible to the mechanic
            time_taken += rank * num_cars * num_cars
            cars -= num_cars  # Reduce the number of cars remaining
            
            if cars == 0:
                break  # All cars have been assigned
        
        return time_taken