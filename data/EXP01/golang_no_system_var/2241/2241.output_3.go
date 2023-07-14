/*
 * @lc app=leetcode id=2241 lang=golang
 *
 * [2241] Design an ATM Machine
 */

type ATM struct {
	banknotesCount []int
}

func Constructor() ATM {
	return ATM{
		banknotesCount: make([]int, 5),
	}
}

func (this *ATM) Deposit(banknotesCount []int) {
	for i := 0; i < len(this.banknotesCount); i++ {
		this.banknotesCount[i] += banknotesCount[i]
	}
}

func (this *ATM) Withdraw(amount int) []int {
	remainingAmount := amount
	result := make([]int, 5)

	for i := 4; i >= 0; i-- {
		numBanknotes := remainingAmount / denominations[i]

		if this.banknotesCount[i] < numBanknotes {
			return []int{-1}
		}

		this.banknotesCount[i] -= numBanknotes
		remainingAmount -= numBanknotes * denominations[i]

		result[i] = numBanknotes
	}

	if remainingAmount > 0 {
		return []int{-1}
	}

	return result
}

var denominations = []int{20, 50, 100, 200, 500}

/**
 * Your ATM object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Deposit(banknotesCount);
 * param_2 := obj.Withdraw(amount);
 */
