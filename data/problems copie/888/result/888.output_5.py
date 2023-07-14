# @lc app=leetcode id=888 lang=python3
class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        total_alice = sum(aliceSizes)
        total_bob = sum(bobSizes)
        diff = (total_alice - total_bob) // 2

        bob_set = set(bobSizes)

        for candy in aliceSizes:
            if candy - diff in bob_set:
                return [candy, candy - diff]