# @lc app=leetcode id=89 lang=python3
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        result = []
        visited = set()
        self.backtrack(n, 0, visited, result)
        return result
    
    def backtrack(self, n: int, num: int, visited: set, result: List[int]):
        result.append(num)
        visited.add(num)
        
        for i in range(n):
            next_num = num ^ (1 << i)  # Flipping one bit at a time
            if next_num not in visited:
                self.backtrack(n, next_num, visited, result)
                break
                
solution = Solution()
n = 2
print(solution.grayCode(n))  # Output: [0, 1, 3, 2]