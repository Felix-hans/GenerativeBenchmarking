# @lc app=leetcode id=2232 lang=python3
class Solution:
    def minimizeResult(self, expression: str) -> str:
        idx = expression.index('+')
        
        num1 = int(expression[:idx])
        num2 = int(expression[idx+1:])
        
        result_no_parentheses = num1 + num2
        
        min_result = result_no_parentheses
        parentheses_pos = (0, 0)
        
        for i in range(1, len(str(num1))):
            for j in range(1, len(str(num2))):
                group1 = int(str(num1)[:i])
                group2 = int(str(num2)[:j])
                
                result_with_parentheses = group1 + group2
                
                new_expression = str(group1) + '+' + str(group2) + '+' + str(num2[j:])
                
                if result_with_parentheses < min_result:
                    min_result = result_with_parentheses
                    parentheses_pos = (i, j)
        
        i, j = parentheses_pos
        new_expression = expression[:i] + '(' + expression[i:idx] + '+' + expression[idx+1:idx+j+1] + ')' + expression[idx+j+1:]
        
        return new_expression