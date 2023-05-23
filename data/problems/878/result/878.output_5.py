# @lc app=leetcode id=878 lang=python3
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return (x * y) // gcd(x, y)

        MOD = 10**9 + 7
        lcm_val = lcm(a, b)
        multiples = n // a + n // b - n // lcm_val
        remaining = n - multiples
        result = (lcm_val * multiples + min(a, b) * remaining) % MOD
        return result