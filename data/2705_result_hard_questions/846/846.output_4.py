# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_counts = {}
        for card in hand:
            card_counts[card] = card_counts.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if card_counts[card] == 0:
                continue

            card_counts[card] -= 1

            for i in range(1, groupSize):
                if card + i not in card_counts or card_counts[card + i] == 0:
                    return False
                card_counts[card + i] -= 1

        return True