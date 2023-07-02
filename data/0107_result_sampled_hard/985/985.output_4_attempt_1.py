# @lc app=leetcode id=985 lang=python3
class Solution:
    def sumEvenAfterQueries(self, nums, queries):
        even_sum = sum(num for num in nums if num % 2 == 0)
        
        answer = []
        
        for val, index in queries:
            nums[index] += val
            
            if nums[index] % 2 == 0:
                even_sum += nums[index]  # Add the updated even value
            elif (nums[index] - val) % 2 == 0:
                even_sum -= val  # Subtract the previous even value
            
            answer.append(even_sum)
        
        return answer