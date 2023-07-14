# @lc app=leetcode id=2266 lang=python3
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            if i > 1 and pressedKeys[i-1] == pressedKeys[i-2]:
                dp[i] = dp[i-1]
            else:
                count = 0
                for j in range(ord(pressedKeys[i-1]) - ord('2') + 1):
                    count += ord(self.getLetter(pressedKeys[i-1])) - ord('a')
                dp[i] = dp[i-1] * count
        
        return dp[n] % (10**9 + 7)
    
    def getLetter(self, digit):
        mapping = {
            '2': 'a',
            '3': 'd',
            '4': 'g',
            '5': 'j',
            '6': 'm',
            '7': 'p',
            '8': 't',
            '9': 'w'
        }
        return mapping[digit]