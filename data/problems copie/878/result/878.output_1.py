# @lc app=leetcode id=878 lang=python3
class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm = (a * b) // self.gcd(a, b)
        low = min(a, b)
        high = n * low

        while low < high:
            mid = (low + high) // 2
            magical_count = mid // a + mid // b - mid // lcm

            if magical_count < n:
                low = mid + 1
            else:
                high = mid

        return low % mod