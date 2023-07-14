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
        
        for i in range(len(hand)):
            if count[hand[i]] > 0:
                for j in range(groupSize):
                    if count.get(hand[i] + j, 0) <= 0:
                        return False
                    count[hand[i] + j] -= 1
        
        return True