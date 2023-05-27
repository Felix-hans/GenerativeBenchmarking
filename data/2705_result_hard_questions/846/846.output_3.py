# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}
        for card in hand:
            count[card] = count.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count.get(card + i, 0) > 0:
                        count[card + i] -= 1
                    else:
                        return False

        return True