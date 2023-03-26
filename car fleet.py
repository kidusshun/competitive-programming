class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pair_list=[]
        for i in range(len(position)):
            pair_list.append((position[i],speed[i]))
        pair_list=sorted(pair_list,key=lambda x:x[0])
        for pair in reversed(pair_list):
            time=(target-pair[0])/pair[1]
            if len(stack)==0:
                stack.append(time)
            elif time<=stack[len(stack)-1]:
                continue
            else:
                stack.append(time)
        return len(stack)