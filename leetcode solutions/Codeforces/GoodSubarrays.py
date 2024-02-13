for _ in range(int(input())):
    n = int(input())
    s = input()
    lst = [int(char) for char in s]
    d = {0:1}
    pref = 0
    ans = 0
    for i,num in enumerate(lst):
        pref +=num
        if pref - i -1 in d:
            ans += d[pref-i-1]
        d[pref-i-1] = d.get(pref-i-1,0)+1
    print(ans)