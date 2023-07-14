# @lc app=leetcode id=2467 lang=python3
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)  # Number of nodes

        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        max_profit = [float('-inf')]  # Maximum net income for Alice

        def dfs(node: int, parent: int, alice_profit: int, gate_count: int) -> None:
            if len(tree[node]) == 1 and tree[node][0] == parent:
                max_profit[0] = max(max_profit[0], alice_profit)
                return

            if node == 0:
                max_profit[0] = max(max_profit[0], amount[node] - alice_profit - gate_count)
                return

            for neighbor in tree[node]:
                if neighbor != parent:
                    curr_profit = (amount[node] + amount[neighbor]) // 2
                    profit_diff = curr_profit - alice_profit
                    new_profit = alice_profit + profit_diff
                    new_gate_count = gate_count + 1

                    dfs(neighbor, node, new_profit, new_gate_count)

        dfs(0, -1, 0, 0)

        return max_profit[0]