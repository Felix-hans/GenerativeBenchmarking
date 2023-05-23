# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        card_count = {}
        for card in hand:
            card_count[card] = card_count.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if card_count[card] == 0:
                continue
            
            card_count[card] -= 1
            
            for i in range(1, groupSize):
                next_card = card + i
                if card_count.get(next_card, 0) > 0:
                    card_count[next_card] -= 1
                else:
                    return False

        return True