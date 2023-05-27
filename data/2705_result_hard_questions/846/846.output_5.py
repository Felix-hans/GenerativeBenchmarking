# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}
        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        for card in sorted(hand):
            if freq[card] > 0:
                for i in range(groupSize):
                    next_card = card + i
                    if next_card not in freq or freq[next_card] <= 0:
                        return False
                    freq[next_card] -= 1

        return True