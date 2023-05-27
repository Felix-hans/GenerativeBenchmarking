# @lc app=leetcode id=846 lang=python3
from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        counter = Counter(hand)
        
        sorted_hand = sorted(hand)
        
        for card in sorted_hand:
            if counter[card] > 0:
                counter[card] -= 1
                
                for i in range(1, groupSize):
                    if counter[card + i] > 0:
                        counter[card + i] -= 1
                    else:
                        return False
        
        return True