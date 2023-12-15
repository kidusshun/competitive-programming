class Bitset:

    def __init__(self, size: int):
        self.bit = ["0"] * size
        self.c = 0
        self.size = size
        self.flipped = ["1"] * size

    def fix(self, idx: int) -> None:
        if self.bit[idx] != "1":
            self.bit[idx] = "1"
            self.flipped[idx] = "0"
            self.c += 1

    def unfix(self, idx: int) -> None:
        if self.bit[idx] != "0":
            self.bit[idx] = "0"
            self.flipped[idx] = "1"
            self.c -= 1

    def flip(self) -> None:
        self.c = self.size - self.c
        self.bit, self.flipped = self.flipped, self.bit

    def all(self) -> bool:
        return self.c == self.size
        

    def one(self) -> bool:
        return self.c >=1
        

    def count(self) -> int:
        val = self.c
        return val

    def toString(self) -> str:
        return "".join(self.bit)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.c()
# param_7 = obj.toString()