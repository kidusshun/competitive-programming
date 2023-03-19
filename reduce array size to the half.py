import collections
def minSetSize(arr: list[int]) -> int:
        hashmap=collections.Counter(arr)
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
print(minSetSize([3,3,3,3,5,5,5,2,2,7]))