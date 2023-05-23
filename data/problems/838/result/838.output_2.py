# @lc app=leetcode id=838 lang=python3
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        forces = []
        force = n = len(dominoes)
        
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
                
            forces.append(force)
            force -= 1
            n -= 1
        
        result = []
        prev = '.'
        
        for i in range(len(forces) - 1, -1, -1):
            net_force = forces[i] - forces[i - 1] if i > 0 else forces[i]
            
            if net_force > 0:
                result.append('R')
            elif net_force < 0:
                result.append('L')
            else:
                result.append(dominoes[i])
                
            prev = result[-1]
            
        return ''.join(result[::-1])