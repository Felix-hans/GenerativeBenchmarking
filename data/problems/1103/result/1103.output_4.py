# @lc app=leetcode id=1103 lang=python3
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people  # Initialize the distribution array
        curr_candies = 1  # Number of candies to be distributed
        
        while candies > 0:
            for i in range(num_people):
                if candies <= 0:
                    break
                ans[i] += min(curr_candies, candies)
                candies -= curr_candies
                curr_candies += 1

        return ans