# @lc app=leetcode id=726 lang=python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        count = {}
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(count)
                count = {}
                i += 1
            elif formula[i] == ')':
                inner_count = count
                count = stack.pop()
                i += 1
                multiplier = 0
                while i < len(formula) and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
                multiplier = max(multiplier, 1)
                for atom, freq in inner_count.items():
                    count[atom] = count.get(atom, 0) + freq * multiplier
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                atom = formula[start:i]
                freq = 0
                while i < len(formula) and formula[i].isdigit():
                    freq = freq * 10 + int(formula[i])
                    i += 1
                freq = max(freq, 1)
                count[atom] = count.get(atom, 0) + freq

        sorted_atoms = sorted(count.keys())
        result = ''
        for atom in sorted_atoms:
            result += atom
            if count[atom] > 1:
                result += str(count[atom])
        return result