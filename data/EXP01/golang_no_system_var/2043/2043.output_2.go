type Bank struct {
    balance []int64
}

func Constructor(balance []int64) Bank {
    return Bank{
        balance: balance,
    }
}

func (b *Bank) isValidAccount(account int) bool {
    return account >= 1 && account <= len(b.balance)
}

func (b *Bank) Transfer(account1, account2 int, money int64) bool {
    if !b.isValidAccount(account1) || !b.isValidAccount(account2) {
        return false
    }

    if b.balance[account1-1] < money {
        return false
    }

    b.balance[account1-1] -= money
    b.balance[account2-1] += money

    return true
}

func (b *Bank) Deposit(account int, money int64) bool {
    if !b.isValidAccount(account) {
        return false
    }

    b.balance[account-1] += money

    return true
}

func (b *Bank) Withdraw(account int, money int64) bool {
    if !b.isValidAccount(account) {
        return false
    }

    if b.balance[account-1] < money {
        return false
    }

    b.balance[account-1] -= money

    return true
}
