# @lc app=leetcode id=838 lang=python3
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Max force applied to the right
            elif dominoes[i] == 'L':
                force = 0  # No force applied to the right
            else:
                force = max(force - 1, 0)  # Decrease force applied to the right gradually
            forces[i] += force

        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n  # Max force applied to the left
            elif dominoes[i] == 'R':
                force = 0  # No force applied to the left
            else:
                force = max(force - 1, 0)  # Decrease force applied to the left gradually
            forces[i] -= force

        result = ''
        for force in forces:
            if force > 0:
                result += 'R'
            elif force < 0:
                result += 'L'
            else:
                result += '.'

        return result