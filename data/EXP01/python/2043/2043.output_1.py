# @lc app=leetcode id=2043 lang=python3
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = [0] + balance # create a 1-indexed balance list by adding a dummy 0 at index 0

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 >= len(self.balance) or account2 < 1 or account2 >= len(self.balance):
            return False
        if self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account >= len(self.balance):
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account >= len(self.balance):
            return False
        if self.balance[account] >= money:
            self.balance[account] -= money
            return True
        else:
            return False