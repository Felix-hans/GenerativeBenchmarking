# @lc app=leetcode id=2564 lang=python3
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        
        prefix_xor = [0] * n
        prefix_xor[0] = int(s[0])
        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i-1] ^ int(s[i])
        
        ans = []
        for query in queries:
            first, second = query
            left, right = -1, -1
            min_len = float('inf')
            
            for i in range(n):
                if prefix_xor[i] ^ first == second:
                    left = i - min_len + 1
                    right = i
                    min_len = right - left + 1
            
            if left == -1:
                ans.append([-1, -1])
            else:
                ans.append([left, right])
        
        return ans