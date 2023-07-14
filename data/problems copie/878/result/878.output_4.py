# @lc app=leetcode id=878 lang=python3
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        mod = 10**9 + 7
        lcm_ab = lcm(a, b)
        left = 1
        right = 10**18  # Set an upper bound to avoid infinite loop
        
        while left < right:
            mid = (left + right) // 2
            magical_numbers = mid // a + mid // b - mid // lcm_ab
            
            if magical_numbers < n:
                left = mid + 1
            else:
                right = mid
        
        return left % mod