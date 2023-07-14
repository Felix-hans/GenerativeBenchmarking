# @lc app=leetcode id=2410 lang=python3
class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        num_matchings = 0
        used_trainers = set()
        
        for player in players:
            for j, trainer in enumerate(trainers):
                if j not in used_trainers and trainer >= player:
                    num_matchings += 1
                    used_trainers.add(j)
                    break
        
        return num_matchings