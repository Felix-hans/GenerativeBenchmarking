# @lc app=leetcode id=878 lang=python3
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return (a * b) // self.gcd(a, b)

    def countMagicalNumbers(self, x, a, b):
        return (x // a) + (x // b) - (x // self.lcm(a, b))

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        left = min(a, b)
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            count = self.countMagicalNumbers(mid, a, b)

            if count < n:
                left = mid + 1
            else:
                right = mid

        return left % (10**9 + 7)