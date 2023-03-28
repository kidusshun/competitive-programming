def hIndex(citations: list[int]) -> int:
    citations=sorted(citations,reverse=True)
    counter=0
    for i,j in enumerate(citations):
        if i<j:
            counter +=1
    return counter
hIndex([100])