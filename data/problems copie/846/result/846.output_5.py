# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_count = {}
        for card in hand:
            card_count[card] = card_count.get(card, 0) + 1

        for card in sorted(card_count):
            count = card_count[card]
            if count > 0:
                for i in range(card, card + groupSize):
                    if card_count.get(i, 0) < count:
                        return False
                    card_count[i] -= count

        return all(count == 0 for count in card_count.values())