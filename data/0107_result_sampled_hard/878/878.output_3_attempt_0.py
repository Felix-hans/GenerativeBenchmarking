# @lc app=leetcode id=878 lang=python3
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        MOD = int(1e9) + 7

        lcm_val = lcm(a, b)

        count = lcm_val // a + lcm_val // b - 1

        complete_ranges = n // count

        remaining_count = n % count

        magical_num = complete_ranges * lcm_val % MOD

        if remaining_count == 0:
            return magical_num

        curr_num = magical_num
        i = 0

        while i < remaining_count:
            curr_num += 1
            if curr_num % a == 0 or curr_num % b == 0:
                i += 1

        return curr_num % MOD