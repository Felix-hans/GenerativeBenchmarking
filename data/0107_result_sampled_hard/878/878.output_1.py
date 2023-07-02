# @lc app=leetcode id=878 lang=python3
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        lcm_ab = lcm(a, b)

        magical_numbers_per_cycle = lcm_ab // a + lcm_ab // b - 1

        complete_cycles = n // magical_numbers_per_cycle
        remaining_numbers = n % magical_numbers_per_cycle

        result = (complete_cycles * lcm_ab) % MOD

        if remaining_numbers == 0:
            return result
        else:
            if complete_cycles == 0:
                for i in range(1, min(a, b) + 1):
                    if i % a == 0 or i % b == 0:
                        remaining_numbers -= 1
                        if remaining_numbers == 0:
                            return i % MOD
            else:
                for i in range(1, min(a, b) + 1):
                    if i % a == 0 or i % b == 0:
                        remaining_numbers -= 1
                        if remaining_numbers == 0:
                            return (result + i) % MOD

        return result