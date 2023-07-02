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

        count_within_period = lcm_ab // a + lcm_ab // b - 1

        complete_periods = n // count_within_period

        remaining = n % count_within_period

        result = complete_periods * lcm_ab

        if remaining == 0:
            return result % MOD

        multiple_a = a
        multiple_b = b

        for _ in range(remaining - 1):
            if (result + multiple_a) < (result + multiple_b):
                result += multiple_a
                multiple_a += a
            else:
                result += multiple_b
                multiple_b += b

        return (result + min(multiple_a, multiple_b)) % MOD