# @lc app=leetcode id=972 lang=python3
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse_number(num_str):
            integer_part = ""
            non_repeating_part = ""
            repeating_part = ""
            
            parts = num_str.split('.')
            
            if parts[0]:
                integer_part = parts[0]
            
            if len(parts) > 1 and parts[1]:
                if '(' in parts[1]:
                    non_repeating_part, repeating_part = parts[1].split('(')
                    repeating_part = repeating_part[:-1]  # Removing the closing bracket
                else:
                    non_repeating_part = parts[1]
            
            return integer_part, non_repeating_part, repeating_part
        
        s_int, s_non_repeating, s_repeating = parse_number(s)
        t_int, t_non_repeating, t_repeating = parse_number(t)
        
        if s_int != t_int:
            return False
        
        if s_non_repeating != t_non_repeating:
            return False
        
        if len(s_repeating) != len(t_repeating):
            return False
        elif s_repeating and t_repeating:
            cycle = s_repeating * (len(t_repeating) // len(s_repeating) + 1)
            if t_repeating not in cycle[:len(t_repeating)]:
                return False
        
        return True