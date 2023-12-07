class Solution:
    def totalMoney(self, n: int) -> int:
        amounts_per_day = [1,2,3,4,5,6,7]
        quotient, remainder = divmod(n,7)
        total_amount =0
        for i in range(quotient):
            total_amount += sum(amounts_per_day) +(7*i)
        for i in range(remainder):
            total_amount += (amounts_per_day[i]+quotient)
        return total_amount