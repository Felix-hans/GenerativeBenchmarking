# @lc app=leetcode id=726 lang=python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []  # Stack to maintain scopes and element counts
        count = {}  # Dictionary to store the count of each element

        i = 0
        while i < len(formula):
            ch = formula[i]

            if ch == '(':
                stack.append(count)  # Save the current count in the stack
                count = {}  # Start a new count for the current scope
                i += 1
            elif ch == ')':
                i += 1
                multiplier = 0
                while i < len(formula) and formula[i].isdigit():
                    multiplier = multiplier * 10 + int(formula[i])
                    i += 1

                if multiplier == 0:
                    multiplier = 1

                top = stack.pop()  # Retrieve the previous count from the stack
                for element, element_count in count.items():
                    top[element] = top.get(element, 0) + element_count * multiplier

                count = top  # Update the count with the combined values
            else:
                element_start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1

                element = formula[element_start:i]

                count_start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1

                element_count = int(formula[count_start:i]) if count_start < i else 1
                count[element] = count.get(element, 0) + element_count

        elements = sorted(count.keys())

        result = ""
        for element in elements:
            result += element
            if count[element] > 1:
                result += str(count[element])

        return result