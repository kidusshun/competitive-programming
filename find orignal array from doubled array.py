changed=[1,3,4,2,6,8]
for num in changed:
    if num*2 in changed and num%2 == 0 and num//2 not in changed:
        lst.append(num)
    print(lst)