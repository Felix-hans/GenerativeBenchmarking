# @lc app=leetcode id=726 lang=python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        counts = {}
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(counts)
                counts = {}
                i += 1
            elif formula[i] == ')':
                i += 1
                multiplier = 0
                while i < n and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1
                multiplier = multiplier if multiplier > 0 else 1
                
                for element, count in counts.items():
                    counts[element] = count * multiplier
                
                prev_counts = stack.pop()
                for element, count in counts.items():
                    prev_counts[element] = prev_counts.get(element, 0) + count
                counts = prev_counts
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[start:i]
                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                count = count if count > 0 else 1
                counts[element] = counts.get(element, 0) + count
        
        elements = sorted(counts.keys())
        result = ""
        for element in elements:
            count = counts[element]
            result += element
            if count > 1:
                result += str(count)
        
        return result