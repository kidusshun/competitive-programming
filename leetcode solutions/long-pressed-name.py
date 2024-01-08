class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name)> len(typed):
            return False
        i,j = 0,0
        while i<= len(name) and j<len(typed):
            if i<len(name) and name[i]==typed[j]:
                j+=1
                i+=1
            elif i!=0 and name[i-1] == typed[j]:
                j+=1
            else:
                return False
        if j==len(typed) and i==len(name):
            return True