# @lc app=leetcode id=552 lang=python3
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7

        ending_P = [1, 1, 0]  # Number of eligible records ending with 'P'
        ending_L = [1, 0, 0]  # Number of eligible records ending with 'L'

        for i in range(2, n + 1):
            new_ending_P = sum(ending_P) % mod  # Update for adding 'P'
            new_ending_L = sum(ending_L) % mod  # Update for adding 'L'

            new_ending_P += sum(ending_P[:-2]) % mod
            new_ending_L += sum(ending_L[:-2]) % mod

            new_ending_L -= ending_P[-2] % mod

            ending_P = [ending_P[1], ending_P[2], new_ending_P]
            ending_L = [ending_L[1], ending_L[2], new_ending_L]

        return (sum(ending_P) + sum(ending_L)) % mod