# @lc app=leetcode id=2410 lang=python3
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        count = 0
        for player in players:
            for i in range(len(trainers)):
                if trainers[i] >= player:
                    count += 1
                    trainers[i] = -1  # Mark the trainer as used
                    break
        
        return count