def kClosest(points,k):
    new=dict()
    for lst in points:
        dist=(lst[0]**2) + (lst[1]**2)
        new[dist]=lst
    val=new.keys()
    sort=sorted(val)
    final=[]
    for i in range(k):
        final.append(new.get(sort[i]))
    print(*final)
kClosest([[0,1],[1,0]], 2)