# @lc app=leetcode id=726 lang=python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        counts = {}
        i = 0

        while i < len(formula):
            if formula[i] == '(':
                stack.append(counts)
                counts = {}
                i += 1
            elif formula[i] == ')':
                curr_counts = counts
                counts = stack.pop()
                i += 1
                factor = 0
                while i < len(formula) and formula[i].isdigit():
                    factor = factor * 10 + int(formula[i])
                    i += 1
                factor = max(factor, 1)
                for element, count in curr_counts.items():
                    counts[element] = counts.get(element, 0) + count * factor
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                element = formula[start:i]
                count = 0
                while i < len(formula) and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                count = max(count, 1)
                counts[element] = counts.get(element, 0) + count

        sorted_elements = sorted(counts.keys())
        result = ''
        for element in sorted_elements:
            result += element
            if counts[element] > 1:
                result += str(counts[element])
        return result