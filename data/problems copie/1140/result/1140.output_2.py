# @lc app=leetcode id=1140 lang=python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        memo = {}
        return dp(0, 1, piles, memo)