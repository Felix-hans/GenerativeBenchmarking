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
        low = 1
        high = n * min(a, b)
        
        while low < high:
            mid = (low + high) // 2
            count = mid // a + mid // b - mid // lcm(a, b)
            
            if count < n:
                low = mid + 1
            else:
                high = mid
        
        return low % MOD