# @lc app=leetcode id=2043 lang=python3
class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._is_valid_account(account1) and self._is_valid_account(account2) and money <= self.balance[account1-1]:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self._is_valid_account(account):
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self._is_valid_account(account) and money <= self.balance[account-1]:
            self.balance[account-1] -= money
            return True
        return False

    def _is_valid_account(self, account: int) -> bool:
        return account >= 1 and account <= len(self.balance)