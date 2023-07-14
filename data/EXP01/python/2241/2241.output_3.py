# @lc app=leetcode id=2241 lang=python3
class ATM:

    def __init__(self):
        self.banknotesCount = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotesCount[i] += banknotesCount[i]

    def withdraw(self, amount):
        remaining = amount
        withdrawalCount = [0, 0, 0, 0, 0]
        denominations = [500, 200, 100, 50, 20]

        for i in range(5):
            withdrawalCount[i] = min(self.banknotesCount[i], remaining // denominations[i])
            remaining -= withdrawalCount[i] * denominations[i]

        if remaining != 0:
            return [-1]

        for i in range(5):
            self.banknotesCount[i] -= withdrawalCount[i]

        return withdrawalCount