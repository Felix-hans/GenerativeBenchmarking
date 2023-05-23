# @lc app=leetcode id=726 lang=python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        i, n = 0, len(formula)
        counts = {}
        
        def parse_number():
            nonlocal i, n
            if i == n or not formula[i].isdigit():
                return 1
            num = 0
            while i < n and formula[i].isdigit():
                num = num * 10 + int(formula[i])
                i += 1
            return num
        
        def parse_element():
            nonlocal i, n
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            return formula[start:i]
        
        def update_counts():
            nonlocal counts, stack
            num = parse_number()
            for element, count in stack.pop().items():
                counts[element] = counts.get(element, 0) + count * num
        
        while i < n:
            if formula[i] == '(':
                stack.append(counts)
                counts = {}
                i += 1
            elif formula[i] == ')':
                i += 1
                update_counts()
            else:
                element = parse_element()
                counts[element] = counts.get(element, 0) + parse_number()
        
        for element, count in stack.pop().items():
            counts[element] = counts.get(element, 0) + count
        
        sorted_counts = sorted(counts.items(), key=lambda x: x[0])
        result = ''
        for element, count in sorted_counts:
            result += element
            if count > 1:
                result += str(count)
        
        return result