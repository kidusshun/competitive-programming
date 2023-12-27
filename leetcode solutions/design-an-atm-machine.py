class ATM:

    def __init__(self):
        self.bank = [0]*5
        self.notes = [20,50,100,200,500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.bank[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        curr = amount
        ans = [0]*5
        for i in range(4,-1,-1):
            compare = curr//self.notes[i]
            if self.bank[i] > compare:
                ans[i]+=compare
                curr-=compare*self.notes[i]
            else:
                ans[i]+=self.bank[i]
                curr -= self.bank[i]*self.notes[i]
        if curr == 0:
            for i in range(5):
                self.bank[i]-=ans[i]
            return ans
        return [-1]



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)