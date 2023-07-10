class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.pos = 0
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.pos + 1] + [url]
        self.pos += 1
        

    def back(self, steps: int) -> str:
        k = self.pos - steps
        if k<=0: 
            self.pos = 0
            return self.stack[0]
        else:
            self.pos = k
            return self.stack[k]

    def forward(self, steps: int) -> str:
        k = self.pos + steps
        if k>=len(self.stack):
            self.pos = len(self.stack) - 1
            return self.stack[-1]
        else:
            self.pos = k
            return self.stack[k]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)