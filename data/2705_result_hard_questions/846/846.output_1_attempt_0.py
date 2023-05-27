# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        cards = sorted(set(hand))

        for card in cards:
            if count.get(card, 0) > 0:
                for i in range(card, card + groupSize):
                    if count.get(i, 0) == 0:
                        return False
                    count[i] -= 1

        return True