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

        low = 1
        high = lcm_val

        while low < high:
            mid = (low + high) // 2
            magical_count = mid // a + mid // b - mid // lcm_val

            if magical_count < remaining_count:
                low = mid + 1
            else:
                high = mid

        return (magical_num + low) % MOD