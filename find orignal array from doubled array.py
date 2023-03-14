class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 != 0:
            return []
        count=collections.Counter(changed)
        print(count)
        changed.sort()
        lst=[]
        for num in changed:
            if num==0 and count[num]>1:
                count[num]-=1
                lst.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num]-=1
                count[num*2]-=1
                lst.append(num)
        print(lst)
        return lst if len(lst) == len(changed)//2 else []