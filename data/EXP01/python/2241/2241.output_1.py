# @lc app=leetcode id=2241 lang=python3
from typing import List

class ATM:
    def __init__(self):
        self.banknotesCount = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.banknotesCount[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        withdrawCount = [0, 0, 0, 0, 0]  # number of banknotes to be handed to the user
        remainingAmount = amount

        for i in range(4, -1, -1):  # starting from the largest denomination
            maxCount = min(remainingAmount // self.denominations[i], self.banknotesCount[i])
            withdrawCount[i] = maxCount
            remainingAmount -= self.denominations[i] * maxCount

        if remainingAmount > 0 or sum(withdrawCount) == 0:
            return [-1]  # unable to withdraw requested amount

        for i in range(5):
            self.banknotesCount[i] -= withdrawCount[i]

        return withdrawCount

    denominations = [20, 50, 100, 200, 500]


atm = ATM()
atm.deposit([0, 0, 1, 2, 1])
print(atm.withdraw(600))
atm.deposit([0, 1, 0, 1, 1])
print(atm.withdraw(600))
print(atm.withdraw(550))