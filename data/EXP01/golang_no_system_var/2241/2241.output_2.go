type ATM struct {
    banknotesCount []int
}

func Constructor() ATM {
    return ATM{banknotesCount: make([]int, 5)}
}

func (a *ATM) Deposit(banknotesCount []int) {
    for i := 0; i < 5; i++ {
        a.banknotesCount[i] += banknotesCount[i]
    }
}

func (a *ATM) Withdraw(amount int) []int {
    withdrawnCount := make([]int, 5)
    denominations := []int{500, 200, 100, 50, 20}

    for i := 0; i < 5; i++ {
        withdrawnCount[i] = min(amount/denominations[i], a.banknotesCount[i])
        amount -= withdrawnCount[i] * denominations[i]
    }

    if amount > 0 {
        return []int{-1}
    }

    for i := 0; i < 5; i++ {
        a.banknotesCount[i] -= withdrawnCount[i]
    }

    return withdrawnCount
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
