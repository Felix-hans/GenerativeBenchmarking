# @lc app=leetcode id=2241 lang=python3
class ATM:

    def __init__(self):
        self.banknotesCount = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.banknotesCount[i] += banknotesCount[i]

    def withdraw(self, amount):
        ans = [0, 0, 0, 0, 0]
        values = [500, 200, 100, 50, 20]

        for i in range(5):
            while self.banknotesCount[i] > 0 and amount >= values[i]:
                amount -= values[i]
                self.banknotesCount[i] -= 1
                ans[i] += 1

        if amount != 0:
            return [-1]

        return ans