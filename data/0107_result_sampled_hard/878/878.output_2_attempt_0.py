# @lc app=leetcode id=878 lang=python3
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm_ab = self.lcm(a, b)

        magical_count = lcm_ab // a + lcm_ab // b - 1

        cycles = n // magical_count

        remaining = n % magical_count

        result = cycles * lcm_ab

        if remaining != 0:
            i = 1
            while True:
                if i % a == 0 or i % b == 0:
                    remaining -= 1
                if remaining == 0:
                    result += i
                    break
                i += 1

        return result % (10**9 + 7)