# @lc app=leetcode id=846 lang=python3
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = {}
        for card in hand:
            counter[card] = counter.get(card, 0) + 1
        
        sorted_hand = sorted(hand)
        
        for card in sorted_hand:
            if counter[card] > 0:
                for i in range(groupSize):
                    if counter.get(card + i, 0) == 0:
                        return False
                    counter[card + i] -= 1
        
        return True