class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0,0]
        self.face = "East"


    def step(self, num: int) -> None:
        steps_left = num%((self.height+self.width-2)*2)
        if steps_left != 0:
            while steps_left > 0:
                if self.face == "East":
                    available_steps = self.width - self.pos[0]-1
                    if steps_left > available_steps:
                        self.pos = [self.pos[0]+available_steps,self.pos[1]]
                        steps_left -=available_steps
                        self.face = "North"
                    else:
                        self.pos = [self.pos[0]+steps_left,self.pos[1]]
                        steps_left = 0
                elif self.face == "North":
                    available_steps = self.height - self.pos[1]-1
                    if steps_left > available_steps:
                        self.pos = [self.pos[0], self.pos[1]+available_steps]
                        steps_left -=available_steps
                        self.face = "West"
                    else:
                        self.pos = [self.pos[0],self.pos[1]+steps_left]
                        steps_left = 0
                elif self.face == "West":
                    available_steps = self.pos[0]
                    if steps_left > available_steps:
                        self.pos = [self.pos[0] - available_steps, self.pos[1]]
                        steps_left -=available_steps
                        self.face = "South"
                    else:
                        self.pos = [self.pos[0]-steps_left,self.pos[1]]
                        steps_left =0
                else:
                    available_steps = self.pos[1]
                    if steps_left > available_steps:
                        self.pos = [self.pos[0], self.pos[1]-available_steps]
                        steps_left -= available_steps
                        self.face = "East"
                    else:
                        self.pos = [self.pos[0], self.pos[1]-steps_left]
                        steps_left = 0
        elif self.pos == [0,0] and self.face =="East":
            self.face = "South"

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.face


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getface()