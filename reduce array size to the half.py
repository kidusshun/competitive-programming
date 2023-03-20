class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap=Counter(arr)
        values=list(hashmap.values())
        values.sort()
        length=len(arr)
        reduced=0
        num=0
        for value in reversed(values):
            if reduced<length//2:
                reduced+=value
                num+=1
            else:
                return num
        return num