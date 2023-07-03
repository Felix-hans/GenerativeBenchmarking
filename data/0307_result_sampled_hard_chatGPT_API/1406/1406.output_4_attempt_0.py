# @lc app=leetcode id=1406 lang=python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            max_score = float('-inf')
            for j in range(1, 4):
                if i + j <= n:
                    max_score = max(max_score, sum(stoneValue[i:i+j]) - dp[i+j])
            dp[i] = max_score
        
        alice_score = dp[0]
        bob_score = sum(stoneValue) - alice_score
        
        if alice_score > bob_score:
            return "Alice"
        elif alice_score < bob_score:
            return "Bob"
        else:
            return "Tie"