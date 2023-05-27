# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        for card in hand:
            if freq[card] > 0:
                for i in range(groupSize):
                    if freq.get(card + i, 0) <= 0:
                        return False
                    freq[card + i] -= 1

        return True