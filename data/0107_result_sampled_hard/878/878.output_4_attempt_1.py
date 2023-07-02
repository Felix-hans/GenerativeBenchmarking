# @lc app=leetcode id=878 lang=python3
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        lcm_ab = self.lcm(a, b)

        magical_count = lcm_ab // a + lcm_ab // b - 1

        complete_cycles = n // magical_count

        remaining_position = n % magical_count

        last_magical_number = complete_cycles * lcm_ab

        if remaining_position == 0:
            result = last_magical_number % mod
        else:
            low, high = 1, lcm_ab
            while low < high:
                mid = (low + high) // 2
                if mid % a == 0 and mid % b == 0:
                    remaining_position -= 1
                if remaining_position == 0:
                    break
                elif mid % a == 0:
                    high = mid - 1
                elif mid % b == 0:
                    low = mid + 1
                else:
                    low = mid + 1

            result = (last_magical_number + mid) % mod

        return result