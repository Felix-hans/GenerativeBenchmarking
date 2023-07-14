# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_counts = {}
        for card in hand:
            card_counts[card] = card_counts.get(card, 0) + 1

        while card_counts:
            min_card = min(card_counts)

            for i in range(min_card, min_card + groupSize):
                if i not in card_counts:
                    return False
                card_counts[i] -= 1
                if card_counts[i] == 0:
                    del card_counts[i]

        return True