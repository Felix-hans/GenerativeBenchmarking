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
        
        if s_repeating == t_repeating:
            return True
        
        if not s_repeating or not t_repeating:
            return False
        
        s_repeat_len = len(s_repeating)
        t_repeat_len = len(t_repeating)
        lcm = (s_repeat_len * t_repeat_len) // math.gcd(s_repeat_len, t_repeat_len)
        
        s_repeating_cycle = s_repeating * (lcm // s_repeat_len)
        t_repeating_cycle = t_repeating * (lcm // t_repeat_len)
        
        return s_repeating_cycle == t_repeating_cycle