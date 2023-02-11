class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed_pointer=0
        popped_pointer=0
        while pushed_pointer < len(popped):
            if pushed[pushed_pointer] != popped[popped_pointer]:
                pushed_pointer += 1
            elif pushed[pushed_pointer] == popped[popped_pointer] and pushed_pointer-1>=0:
                pushed.remove(pushed[pushed_pointer])
                popped.remove(popped[popped_pointer])
                pushed_pointer-=1
            elif pushed[pushed_pointer] == popped[popped_pointer]:
                pushed.remove(pushed[pushed_pointer])
                popped.remove(popped[popped_pointer])
        if len(popped) == 0 and len(pushed) == 0:
            return True
        return False