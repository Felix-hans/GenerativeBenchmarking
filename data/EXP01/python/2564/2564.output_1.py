# @lc app=leetcode id=2564 lang=python3
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        prefix_xor = [0] * (n + 1)
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ int(s[i])
        
        ans = []
        for query in queries:
            left, right = query
            xor_value = prefix_xor[left] ^ prefix_xor[right + 1]
            if xor_value == right - left:
                ans.append([left, right])
            else:
                ans.append([-1, -1])
        
        return ans