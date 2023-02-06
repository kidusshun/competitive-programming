def validateStackSequences(pushed, popped):
        for i in range(len(pushed)):
            if pushed[i] != popped[len(popped)-1-i] and i!=len(popped)-1-i:
                return False
            elif i==len(popped)-1-i:
                return True
validateStackSequences([1,2,3,4,5], [4,5,3,2,1])