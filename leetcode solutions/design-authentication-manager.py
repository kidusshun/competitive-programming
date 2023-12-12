class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.auth = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.auth[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.auth.keys() and currentTime - self.auth[tokenId] < self.timeToLive:
            self.auth[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token, time in self.auth.items():
            if currentTime - time < self.timeToLive:
                count+=1
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)