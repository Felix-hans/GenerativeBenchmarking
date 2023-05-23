# @lc app=leetcode id=878 lang=python3
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        MOD = 10**9 + 7
        
        lcm_ab = lcm(a, b)
        magical_numbers_in_block = lcm_ab // a + lcm_ab // b - 1
        
        q, r = divmod(n, magical_numbers_in_block)
        result = lcm_ab * q % MOD
        
        if r == 0:
            return result
        
        heap = [(a * i, a, b) for i in range(1, a + 1)]
        heapq.heapify(heap)
        
        for _ in range(r - 1):
            num, a, b = heapq.heappop(heap)
            
            if num % b != 0:
                heapq.heappush(heap, (num + a, a, b))
        
        return (result + heap[0][0]) % MOD