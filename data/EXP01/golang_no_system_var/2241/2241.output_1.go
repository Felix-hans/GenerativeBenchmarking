type ATM struct {
    banknotesCount []int
}

func Constructor() ATM {
    return ATM{}
}

func (a *ATM) Deposit(banknotesCount []int) {
    for i := 0; i < len(a.banknotesCount); i++ {
        a.banknotesCount[i] += banknotesCount[i]
    }
}

func (a *ATM) Withdraw(amount int) []int {
    remainingAmount := amount

    withdrawCounts := []int{0, 0, 0, 0, 0}

    for i := 4; i >= 0; i-- {
        numNotes := remainingAmount / denominations[i]

        if numNotes > a.banknotesCount[i] {
            numNotes = a.banknotesCount[i]
        }

        remainingAmount -= numNotes * denominations[i]
        withdrawCounts[i] = numNotes
    }

    if remainingAmount != 0 {
        return []int{-1}
    }

    for i := 0; i < 5; i++ {
        a.banknotesCount[i] -= withdrawCounts[i]
    }

    return withdrawCounts
}

var denominations = []int{20, 50, 100, 200, 500}
